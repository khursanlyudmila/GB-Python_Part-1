"""
2. Напишите функцию группового переименования файлов. Она должна:
a. принимать параметр желаемое конечное имя файлов.
    При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла.
    Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени.
    Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
    К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
"""
import os
from pathlib import Path

def files_rename(directory: int,
                 new_name_end: str,
                 length_number: int,
                 extension_initial:str,
                 extention_finite: str,
                 name_original: range = (0, 4),
                 ):
    """Групповое переименование файлов по заданным параметрам."""
    count_for_name = 1
    if not os.path.exists(directory) or not os.path.isdir(directory):
        os.mkdir(directory)
    for file in os.listdir(directory):
        if file.endswith(extension_initial):
            letters_of_orig_name = os.path.splitext(file)[0][name_original[0]:name_original[1]]
            new_file_name = (f"{letters_of_orig_name}{new_name_end}{str(count_for_name).
                                zfill(length_number)}{extention_finite}")
            os.rename(os.path.join(directory, file), os.path.join(directory, new_file_name))
            count_for_name += 1
    

if __name__ == '__main__':
    files_rename('./files', '_new_', 3, '.png', '.jpg')
    