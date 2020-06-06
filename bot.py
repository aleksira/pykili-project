import telebot
from telebot import apihelper, types
import config
import project_main
from lucky import lucky, lucky_sticker

apihelper.proxy = {'https': 'socks5h://3.17.56.86:9956'}
bot = telebot.TeleBot(config.TOKEN)

keyboard1 = types.ReplyKeyboardMarkup(one_time_keyboard=True)
b1 = types.KeyboardButton('гиперион')
b2 = types.KeyboardButton('русская деревня')
b3 = types.KeyboardButton('ходасевич')
b4 = types.KeyboardButton('циолковский')
b5 = types.KeyboardButton('monitor')
b6 = types.KeyboardButton('primus versus')
keyboard1.add(b1, b2, b3, b4, b5, b6)

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
                         '\n\n2. для того, чтобы узнать краткую справку о нужном книжном и перейти на сайт, скажите /search_shop' +
                         '\n\n3. если вы в настроении немного попутешествовать и узнать больше о самых интересных ' +
                         'книжных магазинах мира, скажите /lucky')

@bot.message_handler(commands=['search_shop'])
def shop_list(message):
    bot.send_message(
        message.chat.id, 'выберите магазин:', reply_markup=keyboard1)

@bot.message_handler(commands=['lucky'])
def lucky_inf(message):
    bot.send_message(message.chat.id, lucky())

@bot.message_handler(commands=['search_book'])
def main_search(message):
    markup = types.ForceReply(selective=False)
    bot.send_message(
        message.chat.id, 'чтобы найти книгу, отправьте сообщение, в котором ' +
                         'будет название книги (в том числе можете просто ввести ' +
                         'ключевые слова) или фамилия автора', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def shop(message):
    if message.text == 'гиперион':
        bot.send_message(message.chat.id, 'Гиперион – https://hyperionbooks.ru\n' +
                         '\nАдрес и время работы:  д. 7–9 с3,  Хохловский переулок, недалеко от станции метро «Китай-Город», ежедневно с 12 до 22.' +
                         '\nВ «Гиперионе» помимо книг продаются изделия хенд-мейда, чай-кофе, домашняя выпечка и происходят культурные мероприятия' +
                         '— концерты, творческие вечера, спектакли, семинары, выставки, кинопоказы, лекции и мастер-классы (все в том числе — и детские).')
    elif message.text == 'русская деревня':
        bot.send_message(message.chat.id, 'Русская деревня – https://hamlet.ru\n' +
                         '\nАдрес и время работы: ул. Рождественка, д. 12,  ежедневно, кроме воскресенья, с 11 до 20 часов.' +
                         '\nПроизводственный кооператив «Русская деревня» (Москва, Рождественка, д. 12) с 1998 года продает в розницу и мелким оптом редкую и малотиражную литературу. ' +
                         'В  магазине продаются столичные и провинциальные издания по истории, этнографии, археологии, литературоведению, ' +
                         'языкознанию, политологии и другим общественным наукам, современная критика, публицистика, ' +
                         'а также неформальная литература различных направлений.')
    elif message.text == 'ходасевич':
        bot.send_message(message.chat.id, 'Ходасевич – http://xodacevich.org\n' +
                         '\nАдрес и время работы: Покровка, 6, 101000. С 11:00 до 22:00 (пт-сб до 23:00), без выходных.' +
                         '\nДешёвые старые и новые книги. Блокноты, винил, открытки. Примут в дар любые ненужные книги! ' +
                         'Классика независимых магазинов Москвы – Покровка, середина мира между подростками ' +
                         'и людьми в костюмах. Доброе, небольшое.')
    elif message.text == 'циолковский':
        bot.send_message(message.chat.id, 'Циолковский – http://www.primuzee.ru\n' +
                         '\nАдрес и время работы:  Пятницкий пер., 8. Ежедневно с 11:00 до 22:00.' +
                         '\n«Циолковский» организован коллективом магазина «Фаланстер» и Фондом развития Политехнического музея.' +
                         '\nНаучпоп, антиквариат, философия, этнография, поэзия, история религий, редкие литпамятники, репринты и малотиражные издания, а также издание ' +
                         'собственных книг. Фаланстер со вкусом первого похода в Политех (лет в пять, когда ничего не понятно, но очень интересно).')
    elif message.text == 'monitor':
        bot.send_message(message.chat.id, '"Monitor book-box" – https://www.monitorbox.ru\n' +
                         '\nАдрес и время работы: Нижняя Сыромятническая ул., д. 10, строение 1; с 11:00 до 22:00.' +
                         '\n("box" - в переводе "лавка") с самого начала был задуман как специализированный книжный магазин для дизайнеров и архитекторов. ' +
                         'Книги об искусстве, о самых разных его видах: архитектуре, живописи, дизайне, фотографии, ' +
                         'музыке, театре и других. Помимо книг об искусстве, у них хорошая подборка детской и художественной литературы, ' +
                         'книги о культуре, философии, истории, психологии, социологии, урбанистике и другой актуальный non-fiction.')
    elif message.text == 'primus versus':
        bot.send_message(message.chat.id, '«Primus Versus» – https://www.primusversus.com/books\n' +
                         '\nАдрес и время работы: ул. Покровка, д. 27. Вход через арку между кафе «Кинза» и салоном красоты «Виртуаль», далее направо в Культурный ' +
                         'центр «Покровские ворота» («Чайная высота»здесь же!). ' +
                         'С понедельника по субботу с 11:00 до 23:00, в воскресенье с 14:00 до 22:00.' +
                         '\n«Primus Versus» — магазин интеллектуальной литературы, где  вы найдете уникальную подборку книг для тех, кто ' +
                         'профессионально изучает историю, философию, психологию и социологию религии, а также христианская литература для ' +
                         'широкого круга читателей; книги по гуманитарным дисциплинам, культуре и искусству; и многое другое.')
    else:
        msg = message.text.lower()
        bot.send_chat_action(message.chat.id, 'typing')
        answer = project_main.main(msg)
        if answer != 'к сожалению, ничего не найдено :(':
            bot.send_message(message.chat.id, answer)
            bot.send_sticker(message.chat.id, lucky_sticker())
        else:
            bot.send_message(message.chat.id, answer)
            bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAALoJl7aKVarqfnOTHNyp2p20hUh8ESDAALfAAOn3YUGIotrmwGoJEAaBA')

bot.polling()
