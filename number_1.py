
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

number = int(input("Введите день недели (1 -7): "))
if number > 5:
    print('выходной')
else:
    print('рабочий день')


