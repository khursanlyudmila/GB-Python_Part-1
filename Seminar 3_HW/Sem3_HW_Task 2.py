"""
2. Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""

from collections import Counter

lst = [1, 4, 'a', 41, (4, 5), 11, 41, 25, 'a', 9, 9, (4, 5)]
dic = Counter(lst)
my_set = set()

for item in lst:
    if lst.count(item) > 1:
        my_set.add(item)
print(f'Исходный список: {dic}')
print(f'Результирующий список: {list(my_set)}')
