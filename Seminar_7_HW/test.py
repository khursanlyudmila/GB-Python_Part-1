import os
import shutil

#print(os.getcwd())
#os.mkdir('functions')

#os.rmdir('functions')
#shutil.rmtree('functions')

#source_file_2 = os.path.join('Seminar_7_HW', 'functions', 'Sem7_HW_Task2.py')
#if os.path.isfile(source_file_2):
shutil.copy2(
    os.path.join('Seminar_7_HW', 'Sem7_HW_Task2.py'),
    os.path.join('Seminar_7_HW', 'functions')
)
os.rename(os.path.join('Seminar_7_HW', 'functions', 'Sem7_HW_Task2.py'), 
          os.path.join('Seminar_7_HW', 'functions', 'group_files_rename.py'))