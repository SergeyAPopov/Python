import telebot
from telebot import types
from random import randint
bot = telebot.TeleBot("5796962083:AAGStYUyVj1zxfJke76zsXGUQdXv3JjwQN8")

game = False
candies = 221

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Добрый день, <b>{message.from_user.first_name}</b>', parse_mode='html')
    bot.send_message(message.chat.id, '<b>Бот учебный, python! </b>', parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width= 2 )
    ch_1 = types.KeyboardButton("/candy_game")
    markup.add(ch_1)  
    bot.send_message(message.chat.id, 'Что будем делать?',reply_markup = markup)


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


bot.infinity_polling()
