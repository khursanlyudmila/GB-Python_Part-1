"""
2. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""

import os

link = 'C:/Documents/Lyudmila/GeekBrains_courses/Repositariy/GB Python_part 1/Seminar 5_HW/Sem5_HW_Task 2.py'

def tuple_from_link(link_line: str) -> tuple:
    "Возвращает путь, имя файла, расширение файла из полученной на вход ссылки."
    path = os.path.split(link_line)
    file_name = os.path.basename(link_line)
    name, extension = os.path.splitext(file_name)
    return path[0], name, extension


print(f'Кортеж: {tuple_from_link(link)}')
