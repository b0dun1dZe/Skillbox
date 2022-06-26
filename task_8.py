print('Задача 8. Сумма ряда')

# Пользователь вводит действительное число
# "х" и точность "precision".

# P.S: Формулу смотреть на сайте :)


# Напишите программу,
# которая по число х вычисляет сумму ряда в точности до precision.


# Операцией возведения в степень и функцией factorial пользоваться нельзя.

# Пример:
# Введите точность: 0.001

# Введите x: 5
# Сумма ряда =  0.2836250150891709


userNumber = float(input('Введите x: '))
userPrecision = float(input('Введите точность: '))


def factorial(a):  # Нахождение факториала
    b = 1
    for i in range(1, a + 1):
        b *= i
    return b


def degree(a, n):  # Возведение в степень
    b = 1
    for i in range(n):
        b *= a
    return b


def total(x, n):  # Формула нахождения суммы ряда
    return degree(-1, n) * (degree(x, 2 * n) / factorial(2 * n))


result = 0
currentStep = 0
while abs(total(userNumber, currentStep)) >= userPrecision:
    result += total(userNumber, currentStep)
    currentStep += 1
print(f'Сумма ряда = {result}')

# Задача решена!
