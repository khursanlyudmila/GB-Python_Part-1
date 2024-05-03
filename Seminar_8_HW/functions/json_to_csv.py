"""
Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
"""
'''
import json

def json_to_csv(name='db.json', res_file='db.csv'):
    with open(name, 'r', encoding='utf-8') as f_json:
        db = json.load(f_json)
    with open(res_file, 'w', encoding='utf-8') as f:
        for k, v in db.items():
            for k2, v2 in v.items():
                print(f"{k},{k2},{v2}", file=f)


if __name__ == '__main__':
    json_to_csv()
    '''
import os
import json
import csv

def json_to_csv(name='db.json', res_file='db.csv'):
    with open(name, 'r', encoding='utf-8') as f_json:
        if os.path.getsize(name) > 0:
            db = json.load(f_json)
        else:
            print(f'Файл {name} не найден')
            return
    
    list_row = []
    for level, value in db.items():
        for id, name in value.items():
            list_row.append({'level': level, 'user_id': id, 'name': name})

    with open(res_file, 'w', encoding='utf-8') as f:
        fieldnames = ['level', 'user_id', 'name']           # заголовок таблицы
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()                                #сохранение первой строки с заголовком
        writer.writerows(list_row)                          #ссохранение списка сдоварей в формате csv в фай


if __name__ == '__main__':
    json_to_csv()