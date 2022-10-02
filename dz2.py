# '1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

number = str(input("Введите число: "))
lst_sum = map(int, list(number.replace('.', '')))
result = sum(lst_sum)
print(result)

# '2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input("Введите число: "))
count = 1
for i in range(number):
    count *= i+1 
    print(count)
   
# '3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# *Пример:*
# - Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]

# условие не совсем понятно. Если говорим о формуле как в задании- получаем набор идентичных чисел. 
# Реализовал через счетчик. вывел промежуточные значения и сумму.

n = int(input("Введите число: "))
summ = 0
for i in range(n):
    res = (1 + 1/(i+1))**(i+1)
    summ +=res
    print(res)
print('Result:', summ)

# '4. Задайте список из 2N+1 элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

from random import randint
n = int(input("Введите n : "))
lst_n = []
for i in range(2*n+1):
    res = randint(-n, n)
    lst_n.append(res)
print('Список элементов:', lst_n)
firstNum = int(input('Введите первую позицию:'))
secondNum = int(input('Введите вторую позицию:'))
if firstNum > 2*n+1 or secondNum > 2*n+1:
    print('Error, element out of range')
else:
    print(lst_n[firstNum] * lst_n[secondNum])

# '5. Реализуйте алгоритм перемешивания списка.

from random import randint, shuffle
n = int(input("Введите n : "))
lst_n = []
for i in range(n):
    res = randint(0,9)
    lst_n.append(res)
print('Базовый список: ', lst_n)
lst_n2 = lst_n
shuffle(lst_n2)
print('Перемешаный список: ', lst_n2)