'''
Вручную создайте список с целыми числами, которые повторяются. Получите новый список, который содержит уникальные (без повтора) элементы исходного списка. 

*Подготовьте два решения, короткое и длинное, которое 
не использует другие коллекции помимо списков.'''

lst = [1, 7, 8, 1, 4, 5]

print(list(set(lst)))

new_lst = []
for i in not lst:
    if i not in new_lst:
        new_lst.append(i)
print(new_lst)