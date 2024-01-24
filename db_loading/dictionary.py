Category = {
    "зефир": ["сахарная пудра", "орех", "агар", "сахар", "коробка", "черная смородина", "фисташка", "миндаль",
              "грецкий орех","глюкозный сироп", "зефир", "твороженный сыр","сливки", "калибо", "пектин", "пакет", "малина",
              "фейхоа", "сублимирован", "бумага для выпечки", "желатин", "фундук", "клубника", "упаковка","пергамент",
              "кондитер", "шоколад", "темный", "белый", "крахмал","какао","пудра","лента","бумага для выпечки"],
    'овощи': ['морковь','тыква','картофель', 'свекла', 'капуста', 'лук', 'чеснок', 'огурцы', 'помидор',
                  'зелень', 'овощи','черри', "томат", "перец", "баклажан", "авокадо","оливки"],
    'фрукты': ['яблоки', "фрукты", 'груша', 'апельсин','персик', 'банан', 'персик', 'абрикос', 'чернослив', 'арбуз',
               'слива', 'дыня', 'вишня', 'киви',"клубника", "черника", "лимон", "черешня","мандарин","хурма","ананас"],
    'молочка': ['молоко', 'кефир', 'творог', 'сметана', 'сыр', 'сливки', 'айран', 'йогурт', "масло", "моцарелла",
                "сулгуни","матцони","пармезан"],
    'мясо': ['колбаса', 'курица', 'шея', 'фарш', 'говядина', 'сосиски', 'мясо',"грудка", "шейка","свинина","ветчина",
             "рыба","окорочка","форель","хамон","салями","бекон"],
    'хлеб': ['шоти', 'хлеб','лаваш',"ромашка","багет","бублик"],
    "яйца": ["яйца",],
    'п/фабрикаты': ['пельмени', 'хинкали', 'курица-гриль', "блинчики","блины"],
    'крупы': ['макароны','спагетти' ,'булгур','мука','рис', "паста", "лапша","горох","овсянка","гречка"],
    "др. продукты": ["Carrefour","Назилбе", "подсолнечное масло", "соус", "майонез", "сода","продукты"
                     "соль", "уксус", "томатная паста","специи", "аджика","арахис","кетчуп","огурчик"],
    'вкусняшки': ['печенье', 'Барни', 'шоколадка', 'сникерс', 'сушки', 'пироженка', 'булочка', 'гамбургер',"симит",
                  "фаст фуд","пицца","MMs","конфеты","мед",'пирожок', 'хачапури', "пирожок", "мороженое", "жвачка", "чипсы","вафли","хот-дог", "круасан"],
    'напитки': ['сок', 'газировка', 'кола', 'компот', 'минералка','чай','кофе', "растворимый", "Борджоми","напиток",
                "мин.вода","бутилирован","спирт","глинтвейн"],
    "животные": ["корм", "котята", "глистогон", "смесь", "паштет", "собак", "несквик", 'бентонит', "пеленки", "кошк",
                 "котам","каниверм"],
    'алкоголь': ['пиво', 'шампанское', 'вино', 'чача', 'коньяк', 'целикаури', 'саперави', 'игристое вино',"консервы"],
    "бытовая химия":["зубная паста","зубщая щетка","порошок", "стиральный порошок", "мыло", "хозяйствен", "шампунь",
                     "жидкость для стирки", "бумага туалет", "стирки","фейри","гель","тряпки"],
    'Уля':['театральная студия',"Уле","Ули", 'театр','подготовка к школе','гимнастика', "канцелярия", "картон",
           "цветная","бумага", "пряники", "кукла","лего", "альбом", "листы", "носки", "маркеры", "скотч","футболка",
           "мастер класс", "Ульяна","занятия", "ДР"],
    'связь': ['телефон', 'интернет', 'минуты', 'magti', 'silknet', "сотовый"],
    'коммуналка': ['газ', 'электричество', 'вода','коммуналка', "ситиком", "citycom","лифт","magti",'Socar'],
    "ремонт": ["гидроизоляция","шлифовк","краска","канализация","ключ","грунтовка","шкурка","гипсов","душ","клей",
               "двери","кухню","шпатель","скотч брайт","труб","радиатор","трапик","фитинг", "правило","анкер",
           "автомат","лампочка","цемент","отопление","раковин", "чашка алмаз", "подложка","порожек"],
    'кафе': ['кафе', 'Dona', 'Дона'],
    "аптека":["аптека", "бинт", "пластины","презерватив", "прокладки"],
    'транспорт':['проезд','такси', "автобус","транспорт","жд","билет"],
    "услуги": ['стрижка',"DHL","ремонт"]
}


import pandas as pd
import numpy as np

# создаю пустую таблицу для заполнения
Dic_df = pd.DataFrame(columns=['name', 'cat'])

# на основании категорий и товаров создаю таблицу DataFrame для поиска по наименованию наподобие Redis
for key, value in Category.items():
    data = {key:value}
    df = pd.DataFrame({'name':value})
    df['cat'] = np.repeat(key, len(value))
    Dic_df = pd.concat([Dic_df, df], ignore_index=True)
Dic_df = Dic_df.sort_values(by='name')
Dic_df['id'] = range(1, len(Dic_df)+1)
Dic_df = Dic_df[["id",'name','cat']]




