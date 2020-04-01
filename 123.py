sum_5 = 0
number_10 = input('Введите 10-ти значное число')
number_10 = int(number_10)
while number_10>0:
    if number_10%10==5:
        sum_5 = sum_5 + 1
    number_10 = number_10//10
print(sum_5)



