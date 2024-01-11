import re
from datetime import datetime
from database.queue import no_subs
from database.expense import Expense
from database.conn_db import add_new_data, get_subname
from time import time

def make_name_price(note: str) -> list:
    # парсит сообщение с тратой на товар и цену, возвращает кортеж (товар, цена)
    pattern_1 = r'(^.+)\s(\d{0,3}[\.|,]?\d{1,2}$)'
    pattern_2 = r"(^\d{0,3}[\.|,]?\d{1,2})\s(.+$)"
    res_1 = re.match(pattern_1, note)
    res_2 = re.match(pattern_2, note)
    if isinstance(res_1, re.Match):
        return res_1[1], res_1[2]
    elif isinstance(res_2, re.Match):
        return res_2[2], res_2[1]

def split_expense(message: str) ->list[str]:
    #если сообщение многострочное, преобразует сообщение в список строк
    res = []
    if '\n' in message:
        return message.split('\n')
    else:
        res.append(message)
        return res

def make_expense(message: str)->Expense:
    # преообразует строчку с тратой в обьект Expense
    name, price = make_name_price(message)
    name = name.lower()
    today = datetime.now().replace(second=0, microsecond=0)
    cat = get_subname(name)
    if cat != None:
        cat = cat[0]
    return Expense(name, cat, price, today, message, False)

def get_categories(row_messages: str)->str:
    # получаю сырое сообщение, распаршенные наименования добавляю в базу данных, вывожу их категории
    messages = split_expense(row_messages)
    # получаю список строк из сообщения
    all_subnames = []
    # создаю пустой список категорий
    for message in messages:
        print(message)
        try:
            expense = make_expense(message)
            if expense.subname != None:
                add_new_data(expense)
                all_subnames.append(expense.subname)
            else:
                #добавляю в очередь товаров без категории
                no_subs.queue((expense.name,expense.price,expense.raw),)
        except TypeError as e:
            all_subnames.append('unrecognized')
            # если сообщение не парсится оно просто записывается в столбец "сырых сообщений" raw
            today = datetime.today().date()
            expense = Expense(None,None,None,today,message, None)
            add_new_data(expense)
            print(f"{e} не понимаю")
    return ', '.join(all_subnames)


print(make_expense('чай 3'))







