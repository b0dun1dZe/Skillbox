#  Вы — один из разработчиков языка программирования Python, и вы пишете специальный математический модуль, который
#  можно было бы просто подключить внутри программы и облегчить жизнь всем программистам.
#  Реализуйте функцию gcd, которая получает два параметра — два числа — и возвращает наибольший общий делитель этих
#  двух чисел.

#  Пример работы программы:
#  Введите первое число: 6
#  Введите второе число: 10
#  НОД = 2


def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


firstNum = int(input('Введите первое число: '))
secondNum = int(input('Введите второе число: '))

print(f'Наибольший общий делитель: {nod(firstNum, secondNum)}')
