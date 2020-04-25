import re
import requests
from bs4 import BeautifulSoup
import xlrd

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


def xodacevich(di): # функция пока не работает
    url = 'http://xodacevich.org/'
    r = requests.get(url, timeout=5)
    soup = BeautifulSoup(r.content, 'html.parser')
    book_folders = soup.find_all(class_='category-item category-item_250x190')
    book_links = book_folders.select('')
    #print(book_folders)
    pass

def main(message):
    answer = ''
    di = primuzee()
    for title in di:
        if message in title.lower():
            break
    price = '\nЦена: ' + di[title][0]
    num = '\nВ наличии: ' + di[title][1]
    theme = '\nКатегория: ' + di[title][2]
    shop = '\nМагазин: ' + di[title][3]
    title = 'Название: ' + title
    answer = title + shop + theme + price + num
    return answer


if __name__ == '__main__':
    main()