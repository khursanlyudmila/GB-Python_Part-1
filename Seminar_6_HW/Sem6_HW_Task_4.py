"""
4. Напишите функцию в шахматный модуль.
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различные случайные варианты и выведите 4 успешных расстановки.
"""

import random as rnd
from Sem6_HW_Task_3 import queens_attack_successfully

def gen_positions() -> list[tuple[int, int]]:
    "Генератор позиций ферзей."
    result = []
    for i in range(8):
        result.append((i, rnd.randint(0, 7)))
    return result


def successfull_positions(quantity_positions):
    "Проверка позиций ферзей на успешность."
    case_ok = 0
    list_ok_positions = []

    while case_ok < quantity_positions:
        generated_position = gen_positions()
        if queens_attack_successfully(generated_position):
            case_ok += 1
            list_ok_positions.append(generated_position)
    for pos in list_ok_positions:
        print(pos)


if __name__=='__main__':
    print(queens_attack_successfully([(1, 1), (5, 2), (8, 3), (6, 4), (3, 5), (7, 6), (2, 7), (4, 8)]))
    successfull_positions(4)
    