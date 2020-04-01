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