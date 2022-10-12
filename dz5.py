# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота

from random import randint, random

storage = 2021
turn = 1
amount = 0 
player = int(input('ВВедите количество игроков, 1 или 2:'))

if player == 1:
    print('--- игра против бота--- ')
elif player ==2:
    print('--- игра 1 на 1 --- ')
else:
    print('Введено не корректное число!')

def check_move(storage):
    if 100 > storage > 28:
        if storage % 28 == 0:
            print('Рекомендованный ход: 27')
        elif storage % 28 == 1:
            print('Рекомендованный ход: 28')
        else:
            print('Рекомендованный ход: ', (storage % 28) -1)
    elif storage <=28 :
        print('Победный ход: ', storage)

def player_turn(storage):
    valid = False
    while not valid:
        try:
            step = int(input('Введите количестко конфет: '))
        except:
            print('incorrect input')
            continue
        if 0 < step < 29:
            if step <= storage:
                valid = True
                return step
            else:
                print('Столько конфет нет!')
        else:
            print('Введено некорректное количество!')

while storage > 0:
    if turn == 1:
        print('В игре конфет: ', storage) 
        check_move(storage)
        amount = player_turn(storage)
        if amount == storage:
            if player == 1:
                print('Вы победили!')
            if player == 2:
                print('Победил первый игрок!')
        storage -= amount
        print('Ваш ход: ', amount, 'В игре осталось конфет: ', storage)
        turn = 2
    elif turn == 2:
        if player == 1:
            amount = randint(1,28)
            if amount == storage:
                print('Вы проиграли!')
            storage -= amount
            print('Ход компьютера: ', amount, 'В игре осталось конфет: ', storage)
            turn = 1
        if player == 2:
            print('В игре конфет: ', storage) 
            check_move(storage)
            amount = player_turn(storage)
            if amount == storage:
                print('Победил второй игрок!')
            storage -= amount
            print('Ващ ход: ', amount, '/n', 'В игре осталось конфет: ', storage)

            turn = 1

 

# Создайте программу для игры в ""Крестики-нолики"".

list = ['1', '2', '3',
        '4', '5', '6',
        '7', '8', '9']
count = 0
player = 0
a = 0
b = 0
win = 0
def game_print(list):
    for i in range(0, len(list),3):
        print(list[i], '|', list[i+1], '|', list[i+2])

def winner(list):
    global win
    if list[0] == list[1] == list[2] or list[3] == list[4] == list[5] or list[6] == list[7] == list[8] or list[0] == list[3] == list[6] or list[1] == list[4] == list[7] or list[2] == list[5] == list[8] or list[0] == list[4] == list[8] or list[2] == list[4] == list[6]:
        print('Victory!')
        win += 1
    return win

print('Игра началась!')
game_print(list)
while count < len(list):
    if player == 0:
        a = int(input('Ход первого игрока, введите позицию (Х): '))-1
        if list[a] == 'X' or list[a] == 'O':
            print('Ход был ранее произведен и не возможен!')
        else:
            list[a] = 'X'
            winner(list)
            if win == 1:
                print('Победил игрок: ', player +1)
                count +=10
            else:
                player = 1
                count+= 1
        game_print(list)

    elif player == 1:
        b = int(input('Ход второго игрока введите позицию (О): '))-1
        if list[b] == 'X' or list[a] == 'O' or 0<b>9:
            print('Ход был ранее произведен или не возможен!')
        else:
            list[b] = 'O'
            winner(list)
            if win == 1:
                print('Победил игрок: ', player +1)
                count +=10
            else:
                player = 0
                count+= 1
        game_print(list)
