# Напишите программу, которая получает целое число и возвращает 
# его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата, а не для решения.
# Дополнительно: Попробуйте избежать дублирования кода 
# в преобразованиях к разным системам счисления.
# Избегайте магических чисел. Добавьте аннотацию типов где это возможно

BASE = 2

number = int(input('Введите число: '))
print(bin(number))
result = ''
while number > BASE:
    result += str(number % BASE)
    number //= BASE
result += str(number)
print(result[::-1])


'''
BASE = 8

number = int(input('Введите число: '))
print(oct(number))
result = ''
while number > BASE:
    result += str(number % BASE)
    number //= BASE
result += str(number)
print(result[::-1])

'''

'''
my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
#print(my_list[2:7:2])
#print(my_list[:7:2])
#print(my_list[2::2])
#print(my_list[2:7:])
print(my_list[:-2]) # весь массив, не вкл. последние 2 цифры

'''