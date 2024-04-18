"""
4. Создайте функцию генератор чисел Фибоначчи
"""

def fibonachi(n):
    a, b = 0, 1
    for _ in range (n):
        yield a
        a, b = b, a + b


number = int(input("Введите число: "))
print(list(fibonachi(number)))
