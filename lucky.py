import random
import requests
from bs4 import BeautifulSoup

def lucky():
    url = 'https://github.com/theodevi/lucky_bookshops/blob/master/lucky_choose.csv'
    r = requests.get(url, timeout=5)
    soup = BeautifulSoup(r.content, 'html.parser')
    soup = soup.find_all(class_='blob-code blob-code-inner js-file-line')
    texts = []
    for i in range(8):
        texts.append(list(soup)[i].get_text())
    r_line = random.choice(texts)
    r_line = r_line.replace(';', '\n')

    return r_line