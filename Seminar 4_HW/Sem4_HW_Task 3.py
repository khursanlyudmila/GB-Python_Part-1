"""
3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""

from decimal import Decimal

MIN_SUM = 50
PROCENT_COMMISION = Decimal(0.015)
MIN_COMISSION = 30
MAX_COMISSION = 600
BONUS = Decimal(0.03)
LIMIT_BEFORE_TAX = 5_000_000
TAX_RATE = Decimal(0.1)

def menu(balance: Decimal, count: int, is_flag: bool):
    """Меню банкомата."""
    dct = {'1': 'Пополнить счет',
           '2': 'Снять со счета',
           '3': 'Операции по счету',
           '4': 'Выйти из программы\n'}

    for k, v in dct.items():
        if k.isdigit():
            print(f'{k}: {v}')
        else:
            print(v)
    
    if balance > LIMIT_BEFORE_TAX:
        balance *= (1 - TAX_RATE)
    choice = input('Введите команду: ')
    if choice == '4':
        print('Будем рады видеть Вас снова!\n')
        is_flag = False
        return balance, is_flag
    elif choice == '1':
        balance = give_money(balance)
        balance_list.append(money_to_give)
    elif choice == '2':
        balance = get_money(balance)
        balance_list.append(-1 * money_to_get) 
    elif choice == '3':
        print('Операции по счету: ', ', '.join(map(str,balance_list)))
    else:
        print('Неверная команда')
    if count % 3 == 0:
        balance *= (1 + BONUS)
        print('Начислены проценты в размере: ', round(balance * BONUS, 2))
    print('Баланс счета: ', round(balance,2))
    print('Счетчик операций: ', count)
    return balance, is_flag


def get_money(balance: Decimal):
    """Возвращает сумму снятия наличности."""
    global money_to_get
    global count
    money_to_get = Decimal(input('Введите сумму снятия: '))
    procent = money_to_get * PROCENT_COMMISION
    if money_to_get % MIN_SUM == 0:
        if procent < MIN_COMISSION:
            procent = MIN_COMISSION
        elif procent > MAX_COMISSION:
            procent = MAX_COMISSION

        if money_to_get + procent <= balance:
            count +=1
            return balance - (money_to_get + procent)
        else:
            print('Недостаточно средств для снятия!')
            return balance
    else:
        print('Ошибка снятия денег, сумма должна быть кратна 50!')
        return balance


def give_money(balance: Decimal):
    """Возвращает сумму пополнения наличности."""
    global money_to_give
    global count
    money_to_give = Decimal(input('Введите сумму пополнения: '))
    if money_to_give % MIN_SUM == 0:
        count +=1
        return balance + money_to_give
    else:
        print('Недостаточно средств для пополнения, сумма не кратна 50!\n')
        return balance


if __name__ == '__main__':
    print('Добро пожаловать в программу банкомат!\n')
    balance = 0
    count = 1
    is_flag = True
    balance_list = []
    while is_flag:
        balance, is_flag = menu(balance, count, is_flag)
        