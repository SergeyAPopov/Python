# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# *В этом случае можно пропустить совсем тривиальные (т.е. задачу 1 или 2 тут точно решать не имеет смысла)

# 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

list = [ i for i in range(1,31) if i%3==0] 
res = sum(list[i] for i in range(len(list)) if i % 2 !=0)
print(list)
print(res)

# # 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# # *Пример:*
# # - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import math

list =list(map(math.factorial,[i+1 for i in range(int(input("Введите число: ")))]))
print('Набор произведений чисел от 1 до N', list)


# 3. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

list1 = [int(input('Введите число:')) for i in range(1,3)]
print(list1)
res = bool(list((list1[i] for i in range(len(list1)) if list1[i-1]**2 == list1[i])))
print(res)

