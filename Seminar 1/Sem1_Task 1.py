'''Посчитайте сумму чётных элементов от 1 до n исключая кратные e. 
Используйте while и if. 
Попробуйте разные значения e и n.'''

n = int(input("Введите число: "))
e = int(input("e: "))
count = 2
sum_1 = 0
while count <= n:
    if count % e == 0:
        count += 2
        continue
    sum_1 += count
    count += 2
    print(" ")
print(sum_1)
