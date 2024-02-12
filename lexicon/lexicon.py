LEXICON: dict[str, str] = {
    '/start': '''<b>Hi!</b> I bot which help you to spend your money wisely )''',
    '/help': '''try text your notes like expence price''',
}

LEXICON_MONTH: dict[str,str] = {
    'jan': 'январь',
    'feb': 'февраль',
    'mar': 'март',
    'apr': 'апрель',
    'may': 'май',
    'jun': 'июнь',
    'jul': 'июль',
    'aug': 'август',
    'sep': 'сентябрь',
    'oct': 'октябрь',
    'nov': 'ноябрь',
    'dec': 'декабрь'}

LEXICON_CANCEL: dict[str, str] = {
    'cancel': 'ОТМЕНИТЬ',
    'add_item': 'Да'}

LEXICON_COMMANDS: dict[str, str] = {
    '/del_last_note': 'удалить последнюю запись',
    '/today': 'траты за сегодня',
    '/week': 'траты за неделю',
    '/month': 'траты за месяц',
    '/my_15': 'мои 15 трат',

}
LEXICON_SUBNAMES: dict[str, str] = {
    'zephyr': 'зефир',
    'ulya': 'Уля',
    'pets': 'животные',
    "farmacy":"аптека",
    'food': 'основные продукты',
    'non_food': 'неосновные продукты',
    'big expenses': 'крупные покупки'}

# зефир
# Уля
# животные
#
# овощи фрукты молочка мясо
# хлеб яйца п/фабрикаты крупы
# др. продукты
#
# алкоголь
# вкусняшки
# напитки
# бытовая химия
# связь
# коммуналка
# ремонт
# кафе
# аптека
# транспорт
# услуги

LEXICON_NOT_BASIC: dict[str, str] = {
    'zephyr': 'зефир',
    'ulya': 'Уля',
    'pets': 'животные',
    "farmacy":"аптека",
    'big expenses': 'крупные покупки'
}

LEXICON_FOOD: dict[str, str] = {
    'vegetables': 'овощи',
    'fruits': 'фрукты',
    'milk': 'молочка',
    'meat':'мясо',
    'bread':'хлеб',
    'eggs':'яйца',
    'semi-finished':'полуфабрикаты',
    'cereals':'крупы',
    'another':'др. продукты'
}

LEXICON_NONFOOD: dict[str, str] = {
    'sweets': 'вкусняшки',
    'drinks': 'напитки',
    'alcohol': 'алкоголь',
    'household_chemicals': 'бытовая химия',
    'cellular':'связь',
    'utilities':'коммуналка',
    'cafe':'кафе',
    'taxi':'транспорт',
    'services':'услуги',
    "renovation": 'ремонт'
}

LEXICON_ANOTHER: dict[str, str] = {
    '_another':'ПОКАЗАТЬ',
    '_cancel': 'ОТМЕНИТЬ',
}

LEXICON_CHOICE = {'LEXICON_NOT_BASIC': LEXICON_NOT_BASIC,
                  'LEXICON_FOOD': LEXICON_FOOD,
                  'LEXICON_NONFOOD':LEXICON_NONFOOD}

LEXICON_KEYS = {key: value for inner_dict in LEXICON_CHOICE.values() for key, value in inner_dict.items()}

def find_value(my_dict, search_key):
    """ищет соответствие категории в объединенном словаре"""
    for dic in my_dict.values():  # проверяем ключ для каждого ключа
        for k,v in dic.items():
            if k == search_key:
                return dic[k]
    return None





