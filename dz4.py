# 1. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from cmath import pi
d = float(input('Введите необходимую точность: '))
count = 0 
while d< 1:
    d *=10
    count+=1
print('Число pi с заданой точностью: ', round(pi, count))

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите число N: '))
list1 = []
def simpl_multiply(number):
    i = 1
    while i <=n:
        if n%i ==0:
            list1.append(i)
        i+=1 

simpl_multiply(n)
print('Список простых множителей заданого числа:', list1)

# 3.Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

list1 = [1,2,3,4,4,5,5,6]
list2 = []
for i in list1:
    if list1.count(i) == 1:
        list2.append(i)
print(list2)


# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from asyncore import write
from random import randint

k = int(input('Введите степень k: '))
x= open('test.txt', 'w')
def generate(n):
    if n ==0:
        return x.write(str(randint(0,100)))
    else:
        x.write(str(randint(0,100)))
        x.write('x**')
        x.write(str(n))
        x.write(' + ')
        # i= randint(0,100),"x**", n,"+"
        return generate(n-1)
result = generate(k)
x.close()


# 5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов. 
# 2*x² + 4*x + 5 3*x² +10*x + 6 
# Вывод: 5*x² + 14*x + 11
import sympy  
a= open('test1.txt', 'r')
b= open('test2.txt', 'r')
x = sympy.Symbol('x')
first_file = a.read()
second_file = b.read()
test1 = first_file + '+ ' + second_file
print(test1)
result = str(sympy.simplify(test1))
print(result)
c= open('test3.txt', 'w')
c.write(result)
a.close()
b.close()
c.close()
