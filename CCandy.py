# На выбор:
# 1. Создайте программу для игры с конфетами человек против человека.
# *' Условие задачи: На столе лежит 117 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
 # a) Добавьте игру против бота

from random import randint

names = ['Грильяж', 'Пралине', 'Марципан']
candy_amount = 117
progress = 117
bot = None
bot_request = ''

bot_request = (input(' Включить игру с ботом? да/нет:  '))

if (bot_request == "да"):
    bot = 1
elif (bot_request == "нет"):
    bot == 0

if (bot == 0):
    first_player_name = input('Введите имя первого игрока: ')
    second_player_name = input('Введите имя второго игрока: ')
else:
    first_player_name = input('Введите имя первого игрока: ')
    second_player_name = names[randint(0, 2)]
    print(f'Твоим соперником будет {second_player_name}!')

first_move = randint(0, 1)
move1 = False

taken_candy1 = 0
taken_candy2 = 0

CCandy = 0

if (first_move == 0):
    move1 = True
for i in range(progress):
    while (candy_amount > 1):
        if (move1 is True):
            CCandy = int(input(f'Ход {first_player_name}, введите количество конфет: '))
            while (CCandy > 28):
                CCandy = int(input(("Может все конфеты сразу взять?), попробуй взять другое количесто: ")))
            while (CCandy < 1):
                CCandy = int(input(("А если все 0 конфет возьмут, что тогда?) попробуй взять другое количесто: ")))
            candy_amount = candy_amount - CCandy
            taken_candy1 += CCandy
            print(f'Количество конфет игрока {first_player_name} = {taken_candy1}')
            CCandy = 0
            move1 = False
        elif (move1 is False and bot == 1):
            print(f'Ходит {second_player_name}')
            CCandy = randint(1, 29)
            print(f'{second_player_name} берет {CCandy} конфет')
            candy_amount = candy_amount - CCandy
            taken_candy2 += CCandy
            print(f'Количество конфет игрока {second_player_name} = {taken_candy2}')
            CCandy = 0
            move1 = True
        else:
            CCandy = int(input(f'Ход {second_player_name}, введите количество конфет: '))
            while (CCandy > 28):
                CCandy = int(input(("Может все конфеты сразу взять?), попробуй взять другое количесто: ")))
            while (CCandy < 1):
                CCandy = int(input(("А если все 0 конфет возьмут, что тогда?) попробуй взять другое количесто: ")))
            candy_amount = candy_amount - CCandy
            taken_candy2 += CCandy
            print(f'Количество конфет игрока {second_player_name} = {taken_candy2}')
            CCandy = 0
            move1 = True
    else:
        if (move1 is False):
            print(f'Конфеты кончились! Последний ход остался на строноне {first_player_name}, поздравляем с подбедой!')
        else:
            print(f'Конфеты кончились! Последний ход остался на строноне {second_player_name}, поздравляем с подбедой!')
    break
