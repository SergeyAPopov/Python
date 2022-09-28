# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
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