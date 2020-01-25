#Задачи на циклы и оператор условия------
'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''

print('Задача 1')
i = 0
while i < 5:
    print( 'Строка ', i, ': 0', sep='')
    i += 1
print('')

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''

print('Задача 2')
sum = 0
for i in range(10):
    answer = int(input('Напишите любую цифру: '))
    if answer == 5:
        sum += 1
print('Количество пятёрок равно:', sum)
print('')

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''

print('Задача 3')
sum = 0
for i in range(1,101):
    sum+=i
print('сумма ряда чисел:', sum)
print('')

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''

print('Задача 4')
result = 1
for i in range(1,11):
    result *= i
print('произведение ряда чисел:', result)
print('')

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

print('Задача 5')
number = 39344026
number = str(number)
for i in range(0, len(number)):
    print(number[i])
print('')

'''
Задача 6
Найти сумму цифр числа.
'''

print('Задача 6')
integer_number = 393440
sum = 0
while integer_number>0:
    sum += integer_number%10
    integer_number = integer_number//10
print('сумма цифр числа:', sum)
print('')

'''
Задача 7
Найти произведение цифр числа.
'''

print('Задача 7')
number = 2639
mult = 1
number = str(number)
for i in range(0, len(number)):
    mult *= int(number[i])
print('произведение цифр числа:', mult)
print('')

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''

print('Задача 8')
integer_number = 333665894
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')
print('')

'''
Задача 9
Найти максимальную цифру в числе
'''

print('Задача 9')
integer_number = 674855678
temp = 0
while integer_number>0:
    if integer_number%10 >= temp:
        temp = integer_number%10
    integer_number = integer_number//10
print('максимальное число:', temp)
print('')

'''
Задача 10
Найти количество цифр 5 в числе
'''

print('Задача 10')
integer_number = 9557974867
temp = 0
while integer_number>0:
    if integer_number%10 == 5:
        temp += 1
    integer_number = integer_number//10
print('количество цифр 5:', temp)
print('')