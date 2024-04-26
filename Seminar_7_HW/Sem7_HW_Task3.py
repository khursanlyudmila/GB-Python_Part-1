"""
3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
"""

import os
import shutil

if not os.path.exists(os.path.join('Seminar_7_HW', 'functions')) or not os.path.isdir(os.path.join('Seminar_7_HW', 'functions')):
    os.mkdir(os.path.join('Seminar_7_HW', 'functions'))
        
source_directory = os.listdir('Seminar_7')
for file in source_directory:
    if 'Sem7_Task' in file:
          source_file = os.path.join('Seminar_7', file)
          if os.path.isfile(source_file):
              shutil.copy2(source_file, os.path.join('Seminar_7_HW', 'functions'))

os.rename(os.path.join('Seminar_7_HW', 'functions', 'Sem7_Task1.py'), 
          os.path.join('Seminar_7_HW', 'functions', 'random_pairs_of_numbers.py'))
os.rename(os.path.join('Seminar_7_HW', 'functions', 'Sem7_Task2.py'), 
          os.path.join('Seminar_7_HW', 'functions', 'file_name_generation.py'))
os.rename(os.path.join('Seminar_7_HW', 'functions', 'Sem7_Task3.py'), 
          os.path.join('Seminar_7_HW', 'functions', 'files_lines_multiplication.py'))
os.rename(os.path.join('Seminar_7_HW', 'functions', 'Sem7_Task4.py'), 
          os.path.join('Seminar_7_HW', 'functions', 'create_files_with_parameters.py'))
os.rename(os.path.join('Seminar_7_HW', 'functions', 'Sem7_Task5.py'), 
          os.path.join('Seminar_7_HW', 'functions', 'create_directory.py'))
os.rename(os.path.join('Seminar_7_HW', 'functions', 'Sem7_Task7.py'), 
          os.path.join('Seminar_7_HW', 'functions', 'sort_files.py'))

if not os.path.exists(os.path.join('Seminar_7_HW', 'functions', '__init__.py')):
     open(os.path.join('Seminar_7_HW', 'functions', '__init__.py'), 'a+')

shutil.copy2(
    os.path.join('Seminar_7_HW', 'Sem7_HW_Task2.py'),
    os.path.join('Seminar_7_HW', 'functions')
)

os.rename(os.path.join('Seminar_7_HW', 'functions', 'Sem7_HW_Task2.py'), 
          os.path.join('Seminar_7_HW', 'functions', 'group_files_rename.py'))
