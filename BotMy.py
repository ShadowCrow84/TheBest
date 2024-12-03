import telebot 
import os
import random
import requests
from telebot import types
    
    # Инициализация бота с использованием его токена
bot = telebot.TeleBot("8015240296:AAEj5fmZYV19zadx_JfmpgnUEowKVWsImzc")
    
    # Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
        bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')
    
    # Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
        count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
        bot.reply_to(message, "he" * count_heh)

@bot.inline_handler(lambda query: query.query == 'video')
def query_video(inline_query):
    try:
        r = types.InlineQueryResultVideo('1',
                                         'https://github.com/eternnoir/pyTelegramBotAPI/blob/master/tests/test_data/test_video.mp4?raw=true',
                                         'video/mp4', 
                                         'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/rooster.jpg',
                                         'Title'
                                         )
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

@bot.message_handler(commands=["poll"])
def create_poll(message):
    bot.send_message(message.chat.id, "English Article Test")
    answer_options = ["a", "an", "the", "-"]

    bot.send_poll(
        chat_id=message.chat.id,
        question="We are going to '' park.",
        options=answer_options,
        type="quiz",
        correct_option_id=2,
        is_anonymous=False,
    )
    # Запуск бота
@bot.message_handler(commands=['mem'])
def send_mem(message):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  


def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
    
    
@bot.message_handler(commands=['duck'])
def duck(message):
        '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
        image_url = get_duck_image_url()
        bot.reply_to(message, image_url)

bot.polling()