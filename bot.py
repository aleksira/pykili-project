import telebot
from telebot import apihelper, types
import config
import project_main


from lucky import lucky

apihelper.proxy = {'https': 'socks5h://96.113.176.101:1080'}
bot = telebot.TeleBot(config.TOKEN)

keyboard1 = types.ReplyKeyboardMarkup(one_time_keyboard=True)
b1 = types.KeyboardButton('гиперион')
b2 = types.KeyboardButton('гнозис')
b3 = types.KeyboardButton('русская деревня')
b4 = types.KeyboardButton('ходасевич')
b5 = types.KeyboardButton('циолковский')
b6 = types.KeyboardButton('monitor')
b7 = types.KeyboardButton('primus versus')
keyboard1.add(b1, b2, b3, b4, b5, b6, b7)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id, 'привет! добро пожаловать в наш путеводитель по независимым книжным москвы ' +
                         '(и чуть-чуть всего мира).\nдля того, чтобы узнать, что здесь можно найти, скажите /help')

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(
        message.chat.id, 'здесь можно найти, в каких независимых книжных в москве есть какие книги.' +
                         '\n\n1. для того, чтобы найти книгу по названию, скажите /search_book' +
                         '\n\n2. для того, чтобы узнать краткую справку о нужном книжном, скажите /search_shop' +
                         '\n\n3. если вы хотите получить рандомную подборку книг определенного жанра, скажите /search_genre ' +
                         '\n\n4. если вы в настроении немного попутешествовать и узнать больше о самых интересных ' +
                         'книжных магазинах мира, скажите /lucky')

@bot.message_handler(commands=['search_shop'])
def shop_list(message):
    bot.send_message(
        message.chat.id, 'выбери магазин:', reply_markup=keyboard1)

@bot.message_handler(commands=['lucky'])
def lucky_inf(message):
    bot.send_message(message.chat.id, lucky())

@bot.message_handler(commands=['search_book'])
def main_search(message):
    markup = types.ForceReply(selective=False)
    bot.send_message(
        message.chat.id, 'чтобы найти книгу, отправьте сообщение, в котором ' +
                         'будет название книги (в том числе можете просто ввести ' +
                         'ключевое слово) или фамилия автора', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def shop(message):
    if message.text == 'гиперион':
        bot.send_message(message.chat.id, 'https://hyperionbooks.ru')
    elif message.text == 'гнозис':
        bot.send_message(message.chat.id, 'http://www.gnosisbooks.ru/new/')
    elif message.text == 'русская деревня':
        bot.send_message(message.chat.id, 'https://hamlet.ru')
    elif message.text == 'ходасевич':
        bot.send_message(message.chat.id, 'http://xodacevich.org')
    elif message.text == 'циолковский':
        bot.send_message(message.chat.id, 'http://www.primuzee.ru')
    elif message.text == 'monitor':
        bot.send_message(message.chat.id, 'https://www.monitorbox.ru')
    elif message.text == 'primus versus':
        bot.send_message(message.chat.id, 'https://www.primusversus.com/books')
    else:
        msg = message.text
        bot.send_chat_action(message.chat.id, 'typing')
        answer = project_main.main(msg)
        bot.send_message(message.chat.id, answer)

bot.polling()
