# Напишите программу, которая вычисляет площадь 
# круга и длину окружности по введённому диаметру. 
# Диаметр не превышает 1000 у.е. 
# Точность вычислений должна составлять не менее 42 знаков после запятой.

import decimal
import math
decimal.getcontext().prec = 50

d = decimal.Decimal(input("введите диаметр до 1000: \n"))
if d > 1000:
    print("слишком большое")
r = d/2
pi = decimal.Decimal(math.pi)
s = pi*r**2
long = 2*pi*r
print(s, long)