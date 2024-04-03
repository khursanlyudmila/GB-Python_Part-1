'''2. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других,
то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.'''

a = int(input("Введите 1-ую сторону квадрата: "))
b = int(input("Введите 2-ую сторону квадрата: "))
c = int(input("Введите 3-ью сторону квадрата: "))
if a + b < c or a + c < b or b + c < a:
    print("Треугольника с такими сторонами не существует!")
else:
    if a != b != c:
        print('Треугольник является разносторонним.')
    if a == b or b == c or a == c:
        print('Треугольник является равнобедренным.')
    if a == b == c:
        print('Треугольник является равносторонним.')