# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions

import math

fr1 = str(input('Введите 1-ую дробь вида "а/b": '))
fr2 = str(input('Введите 2-ую дробь вида "а/b": '))

if int(fr1[2]) == 0 or int(fr2[2]) == 0:
    print("Знаменатели дробей не должны быть равны нулю! Введите другие значения!")
    
if int(fr1[2]) == int(fr2[2]):
    numerator_sum = int(fr1[0]) + int(fr2[0])
    denominator_sum = int(fr1[2])
    numerator_prod = int(fr1[0]) * int(fr2[0])
    denominator_prod = int(fr1[2]) * int(fr2[2])
else:
    denominator_sum = int(fr1[2]) * int(fr2[2])
    numerator_sum = int(fr1[0]) * (denominator_sum / int(fr1[2])) \
        + int(fr2[0]) * (denominator_sum / int(fr2[2]))
    numerator_prod = int(fr1[0]) * int(fr2[0])
    denominator_prod = denominator_sum
print(f'Сумма дробей {fr1} и {fr2} равна {math.floor(numerator_sum)}/{math.floor(denominator_sum)}')
print(f'Произведение дробей {fr1} и {fr2} равно {numerator_prod}/{denominator_prod}')


from fractions import Fraction

fr1_check = Fraction(fr1)
fr2_check= Fraction(fr2)
print("Проверка кода с использованием модуля fractions:")
print(f'Сумма дробей {fr1_check} и {fr2_check} равна {fr1_check + fr2_check}')
print(f'Произведение дробей {fr1_check} и {fr2_check} равно {fr1_check * fr2_check}')

