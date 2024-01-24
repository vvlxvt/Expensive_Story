from fuzzywuzzy import process
from db_loading.dictionary import Category
import re
from exceptions.exceptions import MessageError

def dots(x):
    # замена <,> на <.> в сообщениях
    return x.replace(',', '.')

def message_check(message):
    pattern = r"([\w+\d{0,3}[\.|,]?\d{1,2})"
    if len(message) > 60 and '\n' not in message:
        return True

def pars_message(message: str) -> list:
    if message_check(message):
        return [message, '0']
    else:
    # парсит сообщение из входящей строчки, возвращает список продукт, цена
        pattern_1 = r"([\w+'& \-,.(/)]+) ((?<=\s)\d{0,3}[\.|,]?\d{1,2})"
        pattern_2 = r"(\d{0,3}[\.|,]?\d{1,2}) ((?<=\s)[\w+ ,.\-(/)]+)"
        x1 = re.match(pattern_1, message)
        x2 = re.match(pattern_2, message)
        if isinstance(x1, re.Match):
            return [x1[1], dots(x1[2])]
        elif isinstance(x2, re.Match):
            return [x2[2], dots(x2[1])]
        else:
            return [message, '0']

def find_cat(query):
    # распакую весь словарь в одну строку наименований
    all_values = [value for values in Category.values() for value in values]

    #нахожу лучшее совпадение и процент наименования из словаря с помощью модуля fuzzywuzzy
    best_match, score = process.extractOne(query, all_values)

    best_category = next(category for category, values in Category.items() if best_match in values)
    result = best_category
    return result if score > 70 else 'другое'

# 1. необходимо обьединить 2 функции парсинга в 1
# 2. сообщения которые не парсятся как надо, должны попадать в сырые сообщения без категории и цены
# 3. провести соответствие категорий в выборе категории и парсинге

# mes = 'Получение 200 лари (продажа детской стенки 5000руб)'
# print(message_check(mes))
