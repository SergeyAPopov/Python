from pytube import YouTube
import telebot
from telebot import types
from random import randint
import requests
import json
bot = telebot.TeleBot("5796962083:AAGStYUyVj1zxfJke76zsXGUQdXv3JjwQN8")

game = False
youtube = False
currency = False
candies = 221
data = requests.get('https://cbr-xml-daily.ru/daily_json.js').json()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Добрый день, <b>{message.from_user.first_name}</b>', parse_mode='html')
    bot.send_message(message.chat.id, '<b>Бот учебный, python! </b>', parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 4 )
    ch_1 = types.KeyboardButton("/candy_game")
    ch_2 = types.KeyboardButton('/Youtybe')
    ch_3 = types.KeyboardButton('/Currency')
    ch_4 = types.KeyboardButton('/Stop')
    markup.add(ch_1,ch_2,ch_3,ch_4)  
    bot.send_message(message.chat.id, 'Что будем делать?',reply_markup = markup)

@bot.message_handler(commands=['Stop'])
def game_stop(message):
    global game, youtube, currency
    game = False
    youtube = False
    currency = False
    bot.send_message(message.chat.id, 'Бот остановлен. для запуска нажмите /start')


@bot.message_handler(commands=['candy_game'])
def game_start(message):
    global game
    if not game:
        global candies
        game = True
        turn = bool(randint(0,1))
        bot.send_message(message.chat.id, f'В игре {candies} конфет. {"Игрок" if turn else "Бот"} делает первый ход')
        bot.send_message(message.chat.id, 'Введите число, от 1 до 28') if turn else bot_turn(message)
        if game: turn = not turn

def bot_turn(message):
    global candies, game
    if  0 < candies <= 28:
        step = candies
    else:
        step = randint(1,28)
    if step < candies:
        candies -= step
        bot.send_message(message.chat.id,f'Бот забрал {step} конфет. осталось {candies} конфет')
    else:
        game = False
        bot.send_message(message.chat.id, "Бот выиграл!")
        candies = 221

@bot.message_handler(func = lambda _: game)
def player_turn(message):
    global candies, game
    try:
        step =int(message.text)
        if step > 28:
            bot.send_message(message.chat.id, "Введите число, от 1 до 28!")
        else:
            if step < candies:
                candies -= step
                bot.send_message(message.chat.id, f'осталось {candies} конфет')
                bot_turn(message)
                if game: bot.send_message(message.chat.id, 'Введите число, от 1 до 28.')
            else:
                candies = 0
                game = False
                bot.send_message(message.chat.id, "Вы победили")
                candies = 221
    except:
        bot.send_message(message.chat.id, "Введено не число.")


@bot.message_handler(commands=['Youtybe'])
def start_yt(message):
    global youtube
    if not youtube:
        youtube = True
        bot.send_message(message.chat.id, "Введите ссылку на видео: ")

@bot.message_handler(func = lambda _: youtube)
def yt_vid(message):
    try:
        yt = YouTube(message.text)
        yt.streams.filter(res='360p').first().download(filename=f'{message.chat.id}.mp4')
        video = f'{message.chat.id}.mp4'
        msg = open(video, 'rb')
        bot.send_video(message.chat.id,msg, timeout=10)
        
    except:
        bot.send_message(message.chat.id, "Введите корректную ссылку на видео: ")

@bot.message_handler(commands=['Currency'])
def start_cur(message):
    global currency
    if not currency:
        currency = True
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(telebot.types.InlineKeyboardButton('USD', callback_data='USD'), 
        (telebot.types.InlineKeyboardButton('EUR', callback_data='EUR')),
        (telebot.types.InlineKeyboardButton('CAD', callback_data='CAD')))  
        bot.send_message(message.chat.id,'Какая валюта вас интересует?',reply_markup=keyboard)

@bot.callback_query_handler(func = lambda _:currency)
def button(call):
    global data
    if call.data =='USD':
        result = str(data['Valute']['USD']['Name']) + ':  ' + str(data['Valute']['USD']['Value'])
        bot.send_message(call.message.chat.id,result)
    elif call.data =='EUR':
        result = str(data['Valute']['EUR']['Name']) + ':  ' + str(data['Valute']['EUR']['Value'])
        bot.send_message(call.message.chat.id,result)
    elif call.data =='CAD':
        result = str(data['Valute']['CAD']['Name']) + ':  ' + str(data['Valute']['CAD']['Value']) 
        bot.send_message(call.message.chat.id,result)

bot.infinity_polling()