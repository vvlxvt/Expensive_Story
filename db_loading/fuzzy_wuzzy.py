from fuzzywuzzy import process
from db_loading.dictionary import Category
import re
from exceptions.exceptions import MessageError

def dots(x):
    # замена <,> на <.> в сообщениях
    return x.replace(',', '.')

def pars_message(message: str) -> list:
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
        return ['message', '0']

def find_cat(query):
    all_values = [value for values in Category.values() for value in values]
    best_match, score = process.extractOne(query, all_values)
    best_category = next(category for category, values in Category.items() if best_match in values)
    result = best_category
    return result if score > 70 else 'другое'

# infinity = iter(int, 1)
# for now in infinity:
#     x = input('введите запрос: ')
#     msg = pars_message(x)[0]
#     print(find_cat(msg))
