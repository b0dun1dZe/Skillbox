print('Задача 3. Число наоборот 2')

# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример:

# Введите первое число: 102
# Введите второе число: 123

# Первое число наоборот: 201
# Второе число наоборот: 321

# Сумма: 522
# Сумма наоборот: 225


def reverse(number):
    reverse_number = ''
    while number != 0:
        reverse_number += str(number % 10)
        number //= 10
    return reverse_number


userFirstNumber = int(input('Введите первое число: '))
userSecondNumber = int(input('Введите второе число: '))

print(f'\nПервое число наоборот: {reverse(userFirstNumber)}')
print(f'Второе число наоборот: {reverse(userSecondNumber)}')

print(
    f'\nСумма: {int(reverse(userFirstNumber)) + int(reverse(userSecondNumber))}'
)
print(f'Сумма наоборот: {userFirstNumber + userSecondNumber}')
