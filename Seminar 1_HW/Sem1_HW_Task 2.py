'''3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: “Число является простым,
если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.'''

MIN_NUMBER = 0
MAX_NUMBER = 100000
a = int(input(f'Введите число для проверки от {MIN_NUMBER} до {MAX_NUMBER}: '))
if a > 100000 or a < 0:
    print('Введено число НЕ из указанного диапазона!')
elif a < 4:
    print (f'Число {a} - простое!')
else:
    for i in range(2, int(a ** 0.5 + 1)):
            if a % i == 0:
                print(f'Число {a} - составное!')
                break
    else:
        print (f'Число {a} - простое!')


'''
С помощью функции:

def is_prime(a):
    if a < 2:
        return "Число составное!"
    for i in range(2, int(a ** 0.5 + 1)):
        if a % i == 0:
            return "Число составное!"
    else:
        return "Число простое!"
print(is_prime(int(input("Введите число для проверки: "))))'''
