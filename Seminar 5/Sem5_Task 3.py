"""
Продолжаем развивать задачу 2. 
Возьмите словарь, который вы получили. 
Сохраните его итератор. 
Далее выведите первые 5 пар ключ-значение, 
обращаясь к итератору, а не к словарю.
"""

import sys

text = 'Без труда не вытащишь и рыбку из пруда!'
dictionary = {key: ord(key) for key in text}
iterator = iter(dictionary.items())
print(iterator)
print(type(iterator))
print(sys.getsizeof(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print('Начало цикла: ')
for item in range(5):
    print(next(iterator))
