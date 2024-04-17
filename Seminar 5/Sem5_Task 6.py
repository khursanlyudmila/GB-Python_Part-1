"""
Выведите в консоль таблицу умножения 
от 2х2 до 9х10 как на школьной тетрадке. 
Таблицу создайте в виде однострочного генератора, 
где каждый элемент генератора — отдельный пример таблицы умножения. 
Для вывода результата используйте «принт» 
без перехода на новую строку.
"""

print(*(f"{i} * {j} = {i * j}\t \t" if i < 6 else ("\n")
      for j in range(2, 11) for i in range(2, 7)))
print(' ')       
print(*(f"{i} * {j} = {i * j}\t \t" if i < 10 else ("\n")
      for j in range(2, 11) for i in range(6, 11)))
