#Задачи на циклы и оператор условия

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''

i = 0

while i < 5:
    i += 1
    print(i,'0')

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''

x = 0

for i in range(10):
    n = input('Введите любую цифру: ')
    if '5' in n:
        x += 1

print('Количество введеных цифр 5 равно', x)

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''

sum = 0

for i in range(1,101):
    sum += i
print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''

multiplication = 1

for i in range(1,11):
    multiplication *= i
print(multiplication)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

integer_number = 1993

print(integer_number%10,integer_number//10)

while integer_number>0:
    print(integer_number%10)
    integer_number = integer_number//10

'''
Задача 6
Найти сумму цифр числа.
'''

integer_number = 1993
sum = 0

while integer_number > 0:
    sum += integer_number%10
    integer_number = integer_number//10
print(sum)

'''
Задача 7
Найти произведение цифр числа.
'''

integer_number = 1993
multi = 1

while integer_number > 0:
    multi *= integer_number%10
    integer_number = integer_number//10
print(multi)

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''

integer_number = 100793

while integer_number > 0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''

integer_number = 100793
max = 0

while integer_number > 0:
    if integer_number%10 >= max:
        max = integer_number%10
    integer_number = integer_number//10
print('Максимальная цифра в числе: ', max)

'''
Задача 10
Найти количество цифр 5 в числе
'''

integer_number = 59598
x = 0

while integer_number > 0:
    if integer_number%10 == 5:
        x += 1
    integer_number = integer_number//10
print('Количество цифр 5 в числе: ', x)
