"""
Создайте модуль с функцией внутри. 
Функция получает на вход загадку, список с возможными вариантами отгадок
и количество попыток на угадывание.
Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
"""

def secrets(puzzle: str, answers: list[str], count=3) -> int:
    print(f'Угадай загадку.\n{puzzle}')
    for i in range(1, count+1):
        ans = input(f'Попытка номер {i}: ').lower()
        if ans in answers:
            return i
    return 0


if __name__ == '__main__':
    result = secrets('Зимой и летом одним цветом', ['ель', 'ёлка', 'сосна'])
    print(f'Угадал с {result} попытки' if result > 0 else 'Не угадал')
    