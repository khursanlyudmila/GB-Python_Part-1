'''
Создайте вручную кортеж содержащий элементы разных типов. 
Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа.
'''
tup = (12, "line 1", "line 2", 26.13, 1522, "line 3")
dic_type = {}
for item in tup:
    t = type(item).__name__
    if t not in dic_type:
        dic_type[t] = []
    dic_type[t].append(item)
print(dic_type)