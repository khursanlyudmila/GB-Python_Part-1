"""
Создайте функцию-генератор. 
Функция генерирует N простых чисел, 
начиная с числа 2. 
Для проверки числа на простоту используйте правило:
«число является простым, если делится нацело только на единицу и на себя».
"""
'''
for i in range(2, numb // 2 + 1):
        if numb % i == 0:
            count += 1
    if count <= 0:
        print("Число простое")
'''

def prime(n):
    if n<3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_simple():
    n = 2
    while True:
        if prime(n):
            yield n
        n +=1

j = generate_simple()
for _ in range(int(input("введите число N: "))):
    print(next(j), end=' ')
