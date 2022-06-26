import time
import random


def rock_paper_scissors():
    options = ['камень', 'ножницы', 'бумага']
    comp_choice = random.choice(options)
    user_choice = input('\nВведите "камень", "ножницы" или "бумага": ')
    while user_choice not in ('камень', 'ножницы', 'бумага'):
        user_choice = input(
            '\nОшибка ввода! Введите "камень", "ножницы" или "бумага": ')
    if comp_choice == user_choice:
        print(
            f'\nУ компьютера: {comp_choice}, у вас: {user_choice}\nНичья! Сыграть еще раз?'
        )
        repeat = input('Введите "да" или "нет": ')
        while repeat.lower() not in ('да', 'нет'):
            repeat = input('\033[37m\033[41m{}\033[0m'.format('Ошибка ввода! Введите "да" или "нет": '))
        if repeat.lower() == 'да':
            rock_paper_scissors()
        else:
            main_menu()
    elif comp_choice == 'бумага' and user_choice == 'ножницы':
        print(
            f'\nУ компьютера: {comp_choice}, у вас: {user_choice}\nВы выиграли! Сыграть еще раз?'
        )
        repeat = input('Введите "да" или "нет": ')
        while repeat.lower() not in ('да', 'нет'):
            repeat = input('\033[37m\033[41m{}\033[0m'.format('Ошибка ввода! Введите "да" или "нет": '))
        if repeat.lower() == 'да':
            rock_paper_scissors()
        else:
            main_menu()
    elif comp_choice == 'бумага' and user_choice == 'камень':
        print(
            f'\nУ компьютера: {comp_choice}, у вас: {user_choice}\nВы проиграли! Сыграть еще раз?'
        )
        repeat = input('Введите "да" или "нет": ')
        while repeat.lower() not in ('да', 'нет'):
            repeat = input('\033[37m\033[41m{}\033[0m'.format('Ошибка ввода! Введите "да" или "нет": '))
        if repeat.lower() == 'да':
            rock_paper_scissors()
        else:
            main_menu()
    elif comp_choice == 'камень' and user_choice == 'бумага':
        print(
            f'\nУ компьютера: {comp_choice}, у вас: {user_choice}\nВы выиграли! Сыграть еще раз?'
        )
        repeat = input('Введите "да" или "нет": ')
        while repeat.lower() not in ('да', 'нет'):
            repeat = input('\033[37m\033[41m{}\033[0m'.format('Ошибка ввода! Введите "да" или "нет": '))
        if repeat.lower() == 'да':
            rock_paper_scissors()
        else:
            main_menu()
    elif comp_choice == 'камень' and user_choice == 'ножницы':
        print(
            f'\nУ компьютера: {comp_choice}, у вас: {user_choice}\nВы проиграли! Сыграть еще раз?'
        )
        repeat = input('Введите "да" или "нет": ')
        while repeat.lower() not in ('да', 'нет'):
            repeat = input('\033[37m\033[41m{}\033[0m'.format('Ошибка ввода! Введите "да" или "нет": '))
        if repeat.lower() == 'да':
            rock_paper_scissors()
        else:
            main_menu()
    elif comp_choice == 'ножницы' and user_choice == 'камень':
        print(
            f'\nУ компьютера: {comp_choice}, у вас: {user_choice}\nВы выиграли! Сыграть еще раз?'
        )
        repeat = input('Введите "да" или "нет": ')
        while repeat.lower() not in ('да', 'нет'):
            repeat = input('\033[37m\033[41m{}\033[0m'.format('Ошибка ввода! Введите "да" или "нет": '))
        if repeat.lower() == 'да':
            rock_paper_scissors()
        else:
            main_menu()
    elif comp_choice == 'ножницы' and user_choice == 'бумага':
        print(
            f'\nУ компьютера: {comp_choice}, у вас: {user_choice}\nВы проиграли! Сыграть еще раз?'
        )
        repeat = input('Введите "да" или "нет": ')
        while repeat.lower() not in ('да', 'нет'):
            repeat = input('\033[37m\033[41m{}\033[0m'.format('Ошибка ввода! Введите "да" или "нет": '))
        if repeat.lower() == 'да':
            rock_paper_scissors()
        else:
            main_menu()


def guess_the_number():
    options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    comp_choice = random.choice(options)
    print('\nКомпьютер загадал число. Какое это число? У вас есть',
          '\U00002764 ' * 3)
    for attempt in range(1, 4):
        user_choice = int(input('\nВведите число от "1" до "10": '))
        while user_choice not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
            user_choice = int(input('\033[37m\033[41m{}\033[0m'.format('Ошибка ввода! Введите число от "1" до "10": ')))
        if user_choice == comp_choice:
            print('Вы угадали!')
            break
        elif user_choice < comp_choice:
            if attempt == 3:
                print(f'Вы не угадали! Компьютер загадал число {comp_choice}.')
            else:
                print(
                    'Вы не угадали! Ваше число меньше числа компьютера. Осталось:',
                    '\U00002764 ' * (3 - attempt))
        elif user_choice > comp_choice:
            if attempt == 3:
                print(f'Вы не угадали! Компьютер загадал число {comp_choice}.')
            else:
                print(
                    'Вы не угадали! Ваше число больше числа компьютера. Осталось:',
                    '\U00002764 ' * (3 - attempt))
    print('Игра окончена. Сыграть еще раз?')
    repeat = input('Введите "да" или "нет": ')
    while repeat.lower() not in ('да', 'нет'):
        repeat = input('\033[37m\033[41m{}\033[0m'.format('Ошибка ввода! Введите "да" или "нет": '))
    if repeat.lower() == 'да':
        guess_the_number()
    else:
        main_menu()


def main_menu():
    print('\n\033[37m\033[42m{}\033[0m'.format(
        'Python Interactive Inc. представляет'))
    print('Две игры на выбор: ')
    print('"Камень, ножницы, бумага" - введите "1"')
    print('"Угадай число" - введите "2"')
    user_input = int(input('\nКакую игру вы выбрали: '))
    while user_input not in (1, 2):
        user_input = int(input('Ошибка ввода! Введите "1" или 2": '))
    if user_input == 1:
        print('\nИгра загружается')
        for percent in range(1, 11):
            print(f'Загрузка {percent * 10}%')
            time.sleep(0.2)
        rock_paper_scissors()
    else:
        print('\nИгра загружается')
        for percent in range(1, 11):
            print(f'Загрузка {percent * 10}%')
            time.sleep(0.2)
        guess_the_number()


main_menu()
