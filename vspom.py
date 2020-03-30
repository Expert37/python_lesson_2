'''
for i in range(3):                                      # даем на ввод 3 попытки
    kol_znak = 0
    number_10 = input('Введите десять цифр')
    number_10 = int(number_10)                          # Приводим к типу int
    while number_10>0:
        number_10 = number_10//10
        kol_znak = kol_znak + 1
    if kol_znak==10:
        print('ok')
        break
    else: print('Вы ввели не 10-ти значное число')
'''
for i in range(3):                                      # даем на ввод 10-ти значного числа 3 попытки
    kol_znak = 0
    number_10 = input('Введите десять цифр')
    number_10 = int(number_10)                          # Приводим к типу int
    while number_10>0:
        number_10 = number_10//10
        kol_znak = kol_znak + 1
    if kol_znak==10:
        num_5 = 0
        while number_10>0:
            if number_10%10==5:
                num_5 = num_5 + 1
            number_10 = number_10//10
        print(num_5)
        break
    else: print('Вы ввели не 10-ти значное число')






