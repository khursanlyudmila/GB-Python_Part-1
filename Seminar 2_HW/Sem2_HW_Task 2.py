# 2. Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

BASE = 16

number = int(input('Введите число: '))
print(hex(number))
conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 
                    5: '5', 6: '6', 7: '7', 
                    8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 
                    13: 'd', 14: 'e', 15: 'f'}

result = ''
while number > 0:
    remainder = number % BASE
    result = conversion_table[remainder] + result
    number //= BASE
print(result)