"""
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
Проверку года на високосность вынести в отдельную защищённую функцию.
"""

from datetime import datetime as dt
from calendar import isleap

def check_date(date: str):
    try:
        t = dt.strptime(date, '%d.%m.%Y')
        is_leap(t.year)
        return True
    except:
        return False


def is_leap(year: int):
    print('Високосный' if isleap(year) else 'Не високосный')


if __name__=='__main__':
    print(check_date('25.02.2024'))
