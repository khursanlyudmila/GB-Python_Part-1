"""
2. Напишите функцию, которая получает на вход директорию
и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах,
а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
"""

import os
import json
import csv
import pickle

def get_size(path):
    """Подсчет размера папок, файлов."""
    total = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total += os.path.getsize(fp)
    return total


def directory_walker(dir_path):
    """Сбор информации о папках, файлах."""
    results = []
    for root, dirs, files in os.walk(dir_path):
        for name in files:
            full_path = os.path.join(root, name)
            results.append({"parent_directory": root, 
                            "is_file": True,
                            "name": name,
                            "size_in_bytes": os.path.getsize(full_path)})

        for name in dirs:
            full_path = os.path.join(root, name)
            results.append({"parent_directory": root, 
                            "is_file": False,
                            "name": name,
                            "size_in_bytes": get_size(full_path)})
    return results


def info_to_json(info: dict):
    """Информации о папках, файлах сохраняется в формате *.json."""
    with open((os.path.join('Seminar_8_HW', 'json_file.json')), "w", encoding='utf-8') as f:
        json.dump(info, f, indent=4)


def info_to_csv(info: dict):
    """Информации о папках, файлах сохраняется в формате *.csv."""
    with open((os.path.join('Seminar_8_HW', 'csv_file.csv')), "w", encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=info[0].keys())
        writer.writeheader()
        writer.writerows(info)
       

def info_to_pickle(info: dict):
    """Информации о папках, файлах сохраняется в формате *.pickle."""
    with open((os.path.join('Seminar_8_HW', 'pickle_file.pickle')), "wb") as f:
        pickle.dump(info, f)


if __name__ == '__main__':
    results = directory_walker("./Seminar_7_HW")
    info_to_json(results)
    info_to_csv(results)
    info_to_pickle(results)
