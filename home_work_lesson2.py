#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
print('Решение задачи №1')
number = '0000'
line_number = 1
while line_number<=5:
    print(line_number,number,sep='.')
    line_number = line_number + 1

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
print('Решение задачи №2')
'''
При решении данной задачи не удалось реализовать проверку того, что пользователь вводит именно 10-ти значное число.
'''
sum_5 = 0
number_10 = input('Введите 10-ти значное число')
number_10 = int(number_10)
while number_10>0:
    if number_10%10==5:
        sum_5 = sum_5 + 1
    number_10 = number_10//10
print(sum_5)

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
print('Решение задачи №3')
sum = 0
for i in range(1,101):
   sum = sum + i
print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
print('Решение задачи №4')
proizv = 1
for i in range(1,11):
    proizv = proizv*i
print(proizv)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''
'''
При решении данной задачи не удалось реализовать обратный порядок записи цыфр
'''
print('Решение задачи №5')
integer_number = 4568752
while integer_number>0:
    print(integer_number%10)
    integer_number = integer_number//10

'''
Задача 6
Найти сумму цифр числа.
'''
print('Решение задачи №6')
integer_number = 456
sum_1 = 0
while integer_number>0:
    sum_1 = sum_1 + integer_number%10
    integer_number = integer_number//10
print(sum_1)


'''
Задача 7
Найти произведение цифр числа.
'''
print('Решение задачи №7')
integer_number = 456
proizv = 1
while integer_number>0:
    proizv = proizv * (integer_number%10)
    integer_number = integer_number//10
print(proizv)


'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
print('Решение задачи №8')
integer_number = 1231354
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
print('Решение задачи №9')
max_num = 0
number = None
integer_number = 1235641164712
while integer_number>0:
    number = integer_number%10
    if number>max_num:
        max_num = number
    integer_number = integer_number//10
print(max_num)
'''
Задача 10
Найти количество цифр 5 в числе
'''
print('Решение задачи №10')
num_5 = 0
number_10 = 1234565555
while number_10>0:
    if number_10%10==5:
        num_5 = num_5 + 1
    number_10 = number_10//10
print(num_5)