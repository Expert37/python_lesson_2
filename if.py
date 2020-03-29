# Оператор условия
brand = 'Volvo'         # Брэнд
engine_volume = 2.5     # Объем двигателя
horse_power = 152        # Мощность двигателя
sunroof = True         # Наличие люка

# Проверка условия if
#if horse_power<80:
#    print('No Tax')

# Проверка условия if/else
#if horse_power < 80:print('No Tax')
#else: print('Tax')

# Провека условия if/elif/elif/else
tax = 0
if horse_power<80:
    tax = 0
elif horse_power<100:
    tax = 10000
elif horse_power<150:
    tax = 20000
else:
    tax = 50000
print('Налог=',tax,end='руб.')
print()

# Проверка условия if для присваивания
coolcar = 0                                                         # крутая машина
coolcar = 'машина крутая' if sunroof==1 else 'машина не крутая'     # крутая ли машина. Если есть люк, то 1 иначе 0
print(coolcar)

speed_mashine = 0
speed_mashine = 1 if engine_volume > 2 else 0
print(speed_mashine)