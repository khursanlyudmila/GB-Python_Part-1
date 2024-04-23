"""
2. В модуль с проверкой даты добавьте возможность запуска в терминале
с передачей даты на проверку.
"""

from datetime import datetime as dt
from calendar import isleap
from sys import argv

def check_date(date: str):
    "Проверка корректности введенной даты."
    try:
        t = dt.strptime(date, '%d.%m.%Y')
        is_leap(t.year)
        return True
    except:
        return False


def is_leap(year: int):
    "Проверка года на високосность."
    print('Високосный' if isleap(year) else 'Не високосный')


if __name__=='__main__':
    date = argv[1]
    print(check_date(date))
