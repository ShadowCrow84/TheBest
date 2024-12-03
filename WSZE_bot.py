import telebot 
from telebot import types
bot = telebot.TeleBot('7858121238:AAFHY6_kLFO5O6gNrqPxcTne_pxkWy5i9cQ')

@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name},тебя приветствует бот WSZE!')

@bot.message_handler(commands=['ecology'])
def ecology(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    poll = types.KeyboardButton("Викторина по Экологии ")
    save_eco = types.KeyboardButton("Советы по экологии")
    kb.row(poll)
    bot.send_message(message.from_user.id,'Выберите кнопку',reply_markup=kb)

@bot.message_handler(commands=['poll'])
def create_poll(message):
    bot.send_message(message.chat.id, 'Экологическая викторина ')
    answer_options = ['Не мусорить и не делать костры в не положинных местах','Рубить деревья','Выбрасывать мусор ,где попало',]


    bot.send_poll(
        chat_id=message.chat.id,
        question='Что нужно делать для сохранения экологии?',
        options=answer_options,
        type='quiz',
        correct_option_id=0,
        is_anonymous=False,
    )

@bot.message_handler(commands=['poll'])
def create_poll(message):
    bot.send_message(message.chat.id, 'Экологическая викторина ')
    answer_options = ['Ничего','Губит все живое','Продлевает жизнь',]


    bot.send_poll(
        chat_id=message.chat.id,
        question='Что для нас делает экология?',
        options=answer_options,
        type='quiz',
        correct_option_id=2,
        is_anonymous=False,
    )

@bot.message_handler(commands=['poll'])
def create_poll(message):
    bot.send_message(message.chat.id, 'Экологическая викторина ')
    answer_options = ['Воробьи','Соловьи','Грачи',]


    bot.send_poll(
        chat_id=message.chat.id,
        question='Какие птицы прилетаеют на юг первыми?',
        options=answer_options,
        type='quiz',
        correct_option_id=2,
        is_anonymous=False,
    )

@bot.message_handler(commands=['poll'])
def create_poll(message):
    bot.send_message(message.chat.id, 'Экологическая викторина ')
    answer_options = ['Калина','Черника','Смородина',]


    bot.send_poll(
        chat_id=message.chat.id,
        question='Какая ягод бывает белой, черной, красной?',
        options=answer_options,
        type='quiz',
        correct_option_id=2,
        is_anonymous=False,
    )

@bot.message_handler(commands=['poll'])
def create_poll(message):
    bot.send_message(message.chat.id, 'Экологическая викторина ')
    answer_options = ['Пингвин','Кулистр','Страус',]


    bot.send_poll(
        chat_id=message.chat.id,
        question='Какая птица круглый год ходит во фраке?',
        options=answer_options,
        type='quiz',
        correct_option_id=0,
        is_anonymous=False,
    )
@bot.message_handler(commands=['poll'])
def create_poll(message):
    bot.send_message(message.chat.id, 'Экологическая викторина ')
    answer_options = ['Волка','Дятла','Сову',]


    bot.send_poll(
        chat_id=message.chat.id,
        question='Кого называют сонитаром леса?',
        options=answer_options,
        type='quiz',
        correct_option_id=0,
        is_anonymous=False,
    )

bot.polling()