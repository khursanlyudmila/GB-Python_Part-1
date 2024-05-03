"""
3. Соберите из созданных на уроке и в рамках домашнего задания функций
пакет для работы с файлами разных форматов.
"""

import os
import shutil

if not os.path.exists(os.path.join('Seminar_8_HW', 'functions')) or not os.path.isdir(os.path.join('Seminar_8_HW', 'functions')):
    os.mkdir(os.path.join('Seminar_8_HW', 'functions'))
        
source_directory = os.listdir('Seminar_8')
for file in source_directory:
    if 'Sem8_Task' in file:
          source_file = os.path.join('Seminar_8', file)
          if os.path.isfile(source_file):
              shutil.copy2(source_file, os.path.join('Seminar_8_HW', 'functions'))

os.rename(os.path.join('Seminar_8_HW', 'functions', 'Sem8_Task1.py'), 
          os.path.join('Seminar_8_HW', 'functions', 'text_to_json.py'))
os.rename(os.path.join('Seminar_8_HW', 'functions', 'Sem8_Task2.py'), 
          os.path.join('Seminar_8_HW', 'functions', 'access_users.py'))
os.rename(os.path.join('Seminar_8_HW', 'functions', 'Sem8_Task3.py'), 
          os.path.join('Seminar_8_HW', 'functions', 'json_to_csv.py'))
os.rename(os.path.join('Seminar_8_HW', 'functions', 'Sem8_Task4.py'), 
          os.path.join('Seminar_8_HW', 'functions', 'csv_to_json.py'))
os.rename(os.path.join('Seminar_8_HW', 'functions', 'Sem8_Task5.py'), 
          os.path.join('Seminar_8_HW', 'functions', 'json_to_pickle.py'))
os.rename(os.path.join('Seminar_8_HW', 'functions', 'Sem8_Task6.py'), 
          os.path.join('Seminar_8_HW', 'functions', 'pickle_to_csv.py'))
os.rename(os.path.join('Seminar_8_HW', 'functions', 'Sem8_Task7.py'), 
          os.path.join('Seminar_8_HW', 'functions', 'csv_to_pickles.py'))

if not os.path.exists(os.path.join('Seminar_8_HW', 'functions', '__init__.py')):
     open(os.path.join('Seminar_8_HW', 'functions', '__init__.py'), 'a+')

shutil.copy2(
    os.path.join('Seminar_8_HW', 'Sem_8_HW_Task2.py'),
    os.path.join('Seminar_8_HW', 'functions')
)

os.rename(os.path.join('Seminar_8_HW', 'functions', 'Sem_8_HW_Task2.py'), 
          os.path.join('Seminar_8_HW', 'functions', 'files_info_in_directory.py'))