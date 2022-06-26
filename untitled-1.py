import time, random


def rock_paper_scissors():
    options = ['камень', 'ножницы', 'бумага']
    compChoice = random.choice(options)
    userChoice = input('\nВведите "камень", "ножницы" или "бумага": ')
    while userChoice not in ('камень', 'ножницы', 'бумага'):
        userChoice = input(
            '\nОшибка ввода! Введите "камень", "ножницы" или "бумага": ')
    if compChoice == userChoice:
        print(
            f'\nУ компьютера: {compChoice}, у вас: {userChoice}\nНичья! Сыграть еще раз?'
        )
        repeat = input('Введите "да" или "нет": ')
        while repeat.lower() not in ('да', 'нет'):
            repeat = input('\033[37m\033[41m{}\033[0m'.format('Ошибка ввода! Введите "да" или "нет": ')
        if repeat.lower() == 'да':
            rock_paper_scissors()
        else:
            mainMenu()
    elif compChoice == 'бумага' and userChoice == 'ножницы':
        print(
            f'\nУ компьютера: {compChoice}, у вас: {userChoice}\nВы выиграли! Сыграть еще раз?'
        )
        repeat = input('Введите "да" или "нет": ')
        while repeat.lower() not in ('да', 'нет'):
            repeat = input('\033[37m\033[41m{}\033[0m'.format('Ошибка ввода! Введите "да" или "нет": ')
        if repeat.lower() == 'да':
            rock_paper_scissors()
        else:
            mainMenu()
    elif compChoice == 'бумага' and userChoice == 'камень':
        print(
            f'\nУ компьютера: {compChoice}, у вас: {userChoice}\nВы проиграли! Сыграть еще раз?'
        )
        repeat = input('Введите "да" или "нет": ')
        while repeat.lower() not in ('да', 'нет'):
            repeat = input('\033[37m\033[41m{}\033[0m'.format('Ошибка ввода! Введите "да" или "нет": ')
        if repeat.lower() == 'да':
            rock_paper_scissors()
        else:
            mainMenu()
    elif compChoice == 'камень' and userChoice == 'бумага':
        print(
            f'\nУ компьютера: {compChoice}, у вас: {userChoice}\nВы выиграли! Сыграть еще раз?'
        )
        repeat = input('Введите "да" или "нет": ')
        while repeat.lower() not in ('да', 'нет'):
            repeat = input('\033[37m\033[41m{}\033[0m'.format('Ошибка ввода! Введите "да" или "нет": ')
        if repeat.lower() == 'да':
            rock_paper_scissors()
        else:
            mainMenu()
    elif compChoice == 'камень' and userChoice == 'ножницы':
        print(
            f'\nУ компьютера: {compChoice}, у вас: {userChoice}\nВы проиграли! Сыграть еще раз?'
        )
        repeat = input('Введите "да" или "нет": ')
        while repeat.lower() not in ('да', 'нет'):
            repeat = input('\033[37m\033[41m{}\033[0m'.format('Ошибка ввода! Введите "да" или "нет": ')
        if repeat.lower() == 'да':
            rock_paper_scissors()
        else:
            mainMenu()
    elif compChoice == 'ножницы' and userChoice == 'камень':
        print(
            f'\nУ компьютера: {compChoice}, у вас: {userChoice}\nВы выиграли! Сыграть еще раз?'
        )
        repeat = input('Введите "да" или "нет": ')
        while repeat.lower() not in ('да', 'нет'):
            repeat = input('\033[37m\033[41m{}\033[0m'.format('Ошибка ввода! Введите "да" или "нет": ')
        if repeat.lower() == 'да':
            rock_paper_scissors()
        else:
            mainMenu()
    elif compChoice == 'ножницы' and userChoice == 'бумага':
        print(
            f'\nУ компьютера: {compChoice}, у вас: {userChoice}\nВы проиграли! Сыграть еще раз?'
        )
        repeat = input('Введите "да" или "нет": ')
        while repeat.lower() not in ('да', 'нет'):
            repeat = input('\033[37m\033[41m{}\033[0m'.format('Ошибка ввода! Введите "да" или "нет": ')
        if repeat.lower() == 'да':
            rock_paper_scissors()
        else:
            mainMenu()


def guess_the_number():
    options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    compChoice = random.choice(options)
    print('\nКомпьютер загадал число. Какое это число? У вас есть',
          '\U00002764 ' * 3)
    for attempt in range(1, 4):
        userChoice = int(input('\nВведите число от "1" до "10": '))
        while userChoice not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
          userChoice = int(input('\033[37m\033[41m{}\033[0m'.format('Ошибка ввода! Введите число от "1" до "10": '))
        if userChoice == compChoice:
            print('Вы угадали!')
            break
        elif userChoice < compChoice:
            if attempt == 3:
                print(f'Вы не угадали! Компьютер загадал число {compChoice}.')
            else:
                print(
                    'Вы не угадали! Ваше число меньше числа компьютера. Осталось:',
                    '\U00002764 ' * (3 - attempt))
        elif userChoice > compChoice:
            if attempt == 3:
                print(f'Вы не угадали! Компьютер загадал число {compChoice}.')
            else:
                print(
                    'Вы не угадали! Ваше число больше числа компьютера. Осталось:',
                    '\U00002764 ' * (3 - attempt))
    print('Игра окончена. Сыграть еще раз?')
    repeat = input('Введите "да" или "нет": ')
    while repeat.lower() not in ('да', 'нет'):
        repeat = input('\033[37m\033[41m{}\033[0m'.format('Ошибка ввода! Введите "да" или "нет": ')
    if repeat.lower() == 'да':
        guess_the_number()
    else:
        mainMenu()


def mainMenu():
    print('\n\033[37m\033[42m{}\033[0m'.format(
        'Python Interactive Inc. представляет'))
    print('Две игры на выбор: ')
    print('"Камень, ножницы, бумага" - введите "1"')
    print('"Угадай число" - введите "2"')
    userInput = int(input('\nКакую игру вы выбрали: '))
    while userInput not in (1, 2):
        userInput = int(input('Ошибка ввода! Введите "1" или 2": '))
    if userInput == 1:
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


mainMenu()