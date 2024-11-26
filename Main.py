import telebot
from Bot_logic import gen_pass , gen_emodji
    # Замени '' на токен твоего бота
    # Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("8015240296:AAEj5fmZYV19zadx_JfmpgnUEowKVWsImzc")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
        bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
        bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
        bot.reply_to(message, "Пока! Удачи!")

aaaa@bot.message_handler(commands=['password'])
def send_password(message): 
        password_random = gen_pass(7)
        bot.reply_to(message, password_random)
    
@bot.message_handler(commands=['emodji'])
def send_password(message): 
        emodji = gen_emodji()
        bot.reply_to(message, emodji)
    
    


@bot.message_handler(func=lambda message: True)
def echo_all(message):
        bot.reply_to(message, message.text)
    

bot.polling()
