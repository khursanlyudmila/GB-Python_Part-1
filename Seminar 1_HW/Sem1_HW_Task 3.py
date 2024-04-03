'''4. Программа загадывает число от 0 до 1000.
Необходимо угадать число за 10 попыток.
Программа должна подсказывать “больше” или “меньше” после каждой попытки.
Для генерации случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)'''

import random
'''from random import randintnum'''

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
attempt = 1
comp_num = random.randint(LOWER_LIMIT, UPPER_LIMIT)
print("Программа загадала число. У Вас 10 попыток, чтобы его разгадать!")
while attempt <= 10:
    user_num = int(input(str(attempt) + '-а попытка: '))
    if user_num > comp_num:
        print("Загаданное число меньше.")
    elif user_num < comp_num:
        print("Загаданное число больше.")
    else:
        print("Число угадано с %d-й попытки" % attempt)
        break
    attempt += 1
else:
    print("Все попытки исчерпаны. Было загадано число", comp_num)

