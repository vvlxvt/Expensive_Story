LEXICON: dict[str, str] = {
    '/start': '''<b>Hi!</b> I bot which help you to spend your money wisely )''',
    '/help': '''try text your notes like expence price''',
    'del': '❌',
    'cancel': 'ОТМЕНИТЬ'}

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

LEXICON_CHOICE: dict[str, str] = {
    'cancel': 'ОТМЕНИТЬ',
    'add_item': 'Да'}

LEXICON_COMMANDS: dict[str, str] = {
    '/del_last_note': 'удалить последнюю запись',
    '/today': 'траты за сегодня',
    '/week': 'траты за неделю',
    '/month': 'траты за месяц'
}
LEXICON_SUBNAMES: dict[str, str] = {
    'zephyr': 'зефир',
    'ulya': 'Уля',
    'pets': 'животные',
    'big_expense':'крупные траты',
    'food': 'основные продукты',
    'non_food': 'неосновные\nпродукты и услуги'}

LEXICON_NOT_BASIC: dict[str, str] = {
    'zephyr': 'зефир',
    'ulya': 'Уля',
    'pets': 'животные',
    'big_expense': 'крупные траты'
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
    'another':'другие продукты'
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
     'services':'услуги'
}


Z = LEXICON_FOOD.keys()
print(*Z)