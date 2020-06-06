import re
import requests
from bs4 import BeautifulSoup
import xlrd
import string

def primuzee():
    url = 'http://primuzee.ru/userfiles/file/каталог.xls'
    r = requests.get(url, timeout=5)
    di = {}
    with open('primuzee.xls', 'wb') as file:
        file.write(r.content)
    wb = xlrd.open_workbook('primuzee.xls')
    sh = wb.sheet_by_index(0)
    shop = 'циолковский'
    for rownum in range(sh.nrows):
        row = sh.row_values(rownum)
        if re.search(r'\d', str(row[4])):
            inf = []
            title = row[2]
            price = str(int(row[4]))
            inf.append(price)
            num = str(int(row[3]))
            inf.append(num)
            theme = row[0]
            inf.append(theme)
            inf.append(shop)
            di[title] = inf
    return di

def xodacevich(url):
    di = {}
    inf = []
    r = requests.get(url, timeout=10)
    soup = BeautifulSoup(r.content, 'html.parser')
    if soup.find(class_='product-item__preview product-item__preview_250x190') != None:
        book = soup.find(class_='product-item__preview product-item__preview_250x190')
        url_b = book.get('href')
        shop = 'ходасевич'
        theme = 'без категории'
        r2 = requests.get(url_b, timeout=10)
        soup2 = BeautifulSoup(r2.content, 'html.parser')
        title = soup2.find(class_='product__name show-for-medium').get_text()
        title = re.sub(r'(\s+)([\w+\.\:,\d\-\?!—\)\(/\" ]+)(\s+)', r'\2', title)
        price = soup2.find(class_='product-price-data').get_text()
        exst = soup2.find(class_='product__quanity').get_text()
        exst = re.sub(r'(\s+)(\w+ \w+( \w+)?)(\s+)', r'\2', exst)
        if exst == 'В наличии':
            num = 'есть'
        else:
            num = 'нет'
        inf.append(price)
        inf.append(num)
        inf.append(theme)
        inf.append(shop)
        di[title] = inf
    return di

def monitor(url):
    di = {}
    inf = []
    r = requests.get(url, timeout=10)
    soup = BeautifulSoup(r.content, 'html.parser')
    if soup.find(class_='products-list__img') != None:
        book = soup.find(class_='products-list__img')
        url_b = book.get('href')
        shop = 'monitor'
        theme = 'без категории'
        r2 = requests.get(url_b, timeout=10)
        soup2 = BeautifulSoup(r2.content, 'html.parser')
        title = soup2.find(class_='catalogue__product-name').get_text()
        price = soup2.find(class_='catalogue__price catalogue__price--lg')
        price = list(price.children)[1].get_text()
        exst = soup2.find(class_='products-full-list__status status instock').get_text()
        exst = re.sub(r'(\s+)(\w+ \w+( \w+)?)(\s+)', r'\2', exst)
        if exst == 'На складе':
            num = 'есть'
        else:
            num = 'нет'
        inf.append(price)
        inf.append(num)
        inf.append(theme)
        inf.append(shop)
        di[title] = inf
    return di

def hyperion(url):
    di = {}
    inf = []
    r = requests.get(url, timeout=10)
    soup = BeautifulSoup(r.content, 'html.parser')
    if soup.find(class_='name-actions col-sm-4') != None:
        book = soup.find(class_='name-actions col-sm-4')
        book = book.find('a')
        url_b = book.get('href')
        shop = 'гиперион'
        theme = 'без категории'
        r2 = requests.get(url_b, timeout=10)
        soup2 = BeautifulSoup(r2.content, 'html.parser')
        title = soup2.find(id='title-page').get_text().rstrip()
        price = soup2.find(class_='price-new').get_text()
        num = list(soup2.find(class_='description').children)[-1].lstrip()
        inf.append(price)
        inf.append(num)
        inf.append(theme)
        inf.append(shop)
        di[title] = inf
    return di

def primus_versus(url):
    di = {}
    inf = []
    shop = 'primus versus'
    theme = 'без категории'
    r = requests.get(url, timeout=10)
    soup = BeautifulSoup(r.content, 'html.parser')
    if soup.find(class_='t686__link') != None:
        book_folders = soup.find_all(class_='t686__link')
        book_folders.extend(soup.find_all(class_='t404__link'))
        for folder in book_folders:
            url_f = folder.get('href')
            if url_f[0] == '/':
                url_f = 'https://primusversus.com' + url_f
            r2 = requests.get(url_f, timeout=10)
            soup2 = BeautifulSoup(r2.content, 'html.parser')
            books = soup2.find_all(class_='t744__textwrapper')
            for book in books:
                if book.find(field='title') != None:
                    title = book.find(field='title').get_text()
                else:
                    title = book.find(field='li_title__1558105995913')
                if book.find(field='price') != None:
                    price = book.find(field='price').get_text()
                else:
                    price = book.find(field='li_price__1558105995913')
                num = 'есть'
                inf.append(price)
                inf.append(num)
                inf.append(theme)
                inf.append(shop)
                di[title] = inf
    return di

def main(message):
    answer = 'к сожалению, ничего не найдено :('
    message.replace('-', ' ')
    message = message.translate(str.maketrans('', '', string.punctuation))
    words = message.split()
    search_m = '%20'.join(words)
    search_x = '+'.join(words)
    url_monitor = 'https://monitorbox.ru/search/?search=' + search_m
    url_xodacevich = 'https://xodacevich.org/products/search?sort=0&balance=&categoryId=&min_cost=&max_cost=&page=1&text=' + search_x
    url_hyperion = 'https://hyperionbooks.ru/search?search=' + search_m
    url_primus = 'https://primusversus.com/books'
    di = monitor(url_monitor)
    if di == {}:
        di = xodacevich(url_xodacevich)
    elif di == {}:
        di = hyperion(url_hyperion)
    elif di == {}:
        di = primuzee()
    elif di == {}:
        di = primus_versus(url_primus)
    for title in di:
        title1 = title.lower().translate(str.maketrans('', '', string.punctuation))
        if title1.find(message) != -1 or (title.find(words[0]) != -1 and title.find(words[1]) != -1):
            price = '\nЦена: ' + di[title][0]
            num = '\nВ наличии: ' + di[title][1]
            theme = '\nКатегория: ' + di[title][2]
            shop = '\nМагазин: ' + di[title][3]
            title = 'Название: ' + title
            answer = title + shop + theme + price + num
            break
    return answer

if __name__ == '__main__':
    main()