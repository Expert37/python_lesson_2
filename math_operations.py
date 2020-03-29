'''
a = input('First number')
b = input('Second number')

# приведем их к типу int, т.к. тип переменной, которую возвращает input - это всегда строка!!!
a = int(a)
b = int(b)

# произведем математические операции
print(a+b)
print(a-b)
print(a*b)
result = a/b
print(type(result)) # выведем тип result
print(result)
print(a**2)
'''
# Логические операции
a = True
b = False

# Отрицание
print(not a)

# логическое И
print(a and b)

# логическое ИЛИ
print(a or b)
print()
# операции сравнения
a=10
print(a>100)
print(a<100)
print(a!=100)
print(a<=100)
print(a==100)