#Пользователь вводит число N. Напишите функцию summa_n, которая принимает одно целое положительное число N и находит сумму всех чисел от 1 до N включительно. Функция вызывается два раза: сначала от числа N, а затем от полученной суммы.

#Пример работы программы:
#Введите число: 5
#Сумма от 1 до 5 = 15
#Сумма от 1 до 15 = 120

userInput = int(input('Введите число: '))


def summa_n(number):
    count = 0
    for num in range(1, number + 1):
        count += num
    return count


first_summ = summa_n(userInput)
second_summ = summa_n(first_summ)

print(f'Сумма от 1 до {userInput} будет {first_summ}')
print(f'Сумма от 1 до {first_summ} будет {second_summ}')