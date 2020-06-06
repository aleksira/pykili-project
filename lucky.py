import random
import requests
from bs4 import BeautifulSoup

def lucky():
    url = 'https://github.com/theodevi/lucky_bookshops/blob/master/lucky_choose.csv'
    r = requests.get(url, timeout=10)
    soup = BeautifulSoup(r.content, 'html.parser')
    soup = soup.find_all(class_='blob-code blob-code-inner js-file-line')
    texts = []
    for i in range(8):
        texts.append(list(soup)[i].get_text())
    r_line = random.choice(texts)
    r_line = r_line.replace(';', '\n')
    return r_line

def lucky_sticker():
    s1 = 'CAACAgQAAxkBAALoMl7aKXb7mCqpCqWEaJAyOwWyIx5uAALrAAOn3YUGPscXzVvsQ7kaBA'
    s2 = 'CAACAgQAAxkBAALoMF7aKXO8_zPzZLCu8p0H-9ZZGTSbAALvAAOn3YUGMzDiUmGIPRQaBA'
    s3 = 'CAACAgQAAxkBAALoLl7aKXGQisKu1jn_oEDNsiKBMYPeAAKQAAOn3YUG5mNbGbRyO88aBA'
    s4 = 'CAACAgQAAxkBAALoLF7aKW8ymxfjlVLt-1IRHNBicNlHAAIzAAOn3YUGdOr5a3KmRG0aBA'
    s5 = 'CAACAgQAAxkBAALoKl7aKWy6cUJeeYtF88EOdxBtZIDUAALPAAOn3YUGJyZ-DQKkvhgaBA'
    s6 = 'CAACAgQAAxkBAALoKF7aKWmrWOiBpp4wAAFfJ2Wa13yWcQACKQIAAqfdhQZm7xY40Li_pRoE'
    stickers = [s1, s2, s3, s4, s5, s6]
    sticker = random.choice(stickers)
    return sticker