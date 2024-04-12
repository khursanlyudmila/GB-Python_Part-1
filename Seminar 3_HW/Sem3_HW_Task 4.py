"""
4. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
"""

backpack = {
    "палатка": 3.0,
    "спальник": 0.6,
    "пенка": 0.2,
    "одежда": 0.8,
    "обувь": 0.4,
    "еда": 1.5,
    "напитки": 0.7,
    "посуда": 0.9,
    "техника": 0.5,
    "мелочь": 0.1,
}

backpack_size = 5.5
backpack_with_things_by_keys = []
backpack_with_things_by_values = []
weight_things_by_keys = 0
weight_things_by_values = 0
things_sorted_by_keys = sorted(backpack.items())
things_sorted_by_values = sorted(backpack.items(), key=lambda x: x[1])

for i in things_sorted_by_keys:
    if (weight_things_by_keys + i[1]) <= backpack_size:
        weight_things_by_keys += i[1]
        backpack_with_things_by_keys.append(i[0])

for i in things_sorted_by_values:
    if (weight_things_by_values + i[1]) <= backpack_size:
        weight_things_by_values += i[1]
        backpack_with_things_by_values.append(i[0])

print('Наполнение рюкзака, исходя из вещей, отсортированных в алфавитном порядке: ',\
       ', '.join(backpack_with_things_by_keys))
print('Максимальный вес такого рюкзака: ', weight_things_by_keys)     
print('Наполнение рюкзака, исходя из вещей, отсортированных по весу: ',\
       ', '.join(backpack_with_things_by_values))
print('Максимальный вес такого рюкзака: ', weight_things_by_values)
