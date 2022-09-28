# Task1
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

print('input number of day')
day = int(input())
if day == 6 or day == 7:
    print('yes')
elif day < 1 or day > 7:
    print('error 404 ')
else:
    print('no')

# Task2
#  Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.  
#  ¬ not 
# ⋁ or

print('input X, Y, Z,')
X, Y, Z = bool(input()), bool(input()), bool(input())
print(not(X and Y and Z) == (not X and not Y and not Z))

# Task3
# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print('Введите координаты точек X, Y')
X, Y = int(input()), int(input())
if X == 0 or Y == 0:
    print('error 404')
elif X > 0 and Y > 0:
    print('1 четверть')
elif X < 0 and Y > 0:
    print('2 четверть')
elif X < 0 and Y < 0:
    print('3 четверть')
elif X > 0 and Y < 0:
    print('4 четверть')

# Task4
# Напишите программу, которая по заданному номеру четверти, показывает диапазон 
# возможных координат точек в этой четверти (x и y).

print('Введите номер четверти')
quarter = int(input())
if quarter < 0 or quarter > 4:
    print('Error, incorrect input')
elif quarter == 1:
    print('X >= 0, Y >= 0')
elif quarter == 2:
    print('X <= 0, Y >= 0')
elif quarter == 3:
    print('X <= 0, Y <= 0')    
elif quarter == 4:
    print('X >= 0, Y >= 0')

# Task5
# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print('Введите координаты точки А')
Ax, Ay = int(input()), int(input())
print('Введите координаты точки В')
Bx, By = int(input()), int(input())
print('Расстояние между точками:')
print(round(((Bx - Ax)**2 + (By - Ay)**2)**0.5, 2))