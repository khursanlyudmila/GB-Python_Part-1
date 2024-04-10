'''
Пользователь вводит данные. Сделайте проверку данных 
и преобразуйте если возможно в один из вариантов ниже:
Целое положительное число
Вещественное положительное или отрицательное число
Строку в нижнем регистре, если в строке есть 
хотя бы одна заглавная буква
Строку в верхнем регистре в остальных случаях
'''

data = input('Введите данные')

if data.isdecimal():
    print(f'{int(data)} - целое число')
else:
    try:
        print(f"{float(data)} - вещественное число")
    except ValueError:
        if data.lower() != data:
            print(data.lower())
        else:
            print(data.upper())