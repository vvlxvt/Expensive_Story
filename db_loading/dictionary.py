Category = {
    "зефир": ["сахарная пудра", "орех", "агар", "сахар", "коробка", "черная смородина", "фисташка", "миндаль",
              "грецкий орех","глюкозный сироп", "зефир", "твороженный сыр","сливки", "калибо", "пектин", "пакет", "малина",
              "фейхоа", "сублимирован", "бумага для выпечки", "желатин", "фундук", "клубника", "упаковка",
              "кондитер", "шоколад", "темный", "белый", "крахмал","какао","пудра","лента"],
    'овощи': ['морковь','тыква','картофель', 'свекла', 'капуста', 'лук', 'чеснок', 'огурцы', 'помидор',
                  'зелень', 'овощи','черри', "томат", "перец", "баклажан", "авокадо","оливки"],
    'фрукты': ['яблоки', "фрукты", 'груша', 'апельсин','персик', 'банан', 'персик', 'абрикос', 'чернослив', 'арбуз',
               'слива', 'дыня', 'вишня', 'киви',"клубника", "черника", "лимон", "черешня","мандарин","хурма","ананас"],
    'молочка': ['молоко', 'кефир', 'творог', 'сметана', 'сыр', 'сливки', 'айран', 'йогурт', "масло", "моцарелла",
                "сулгуни","матцони","пармезан"],
    'мясо': ['колбаса', 'курица', 'шея', 'фарш', 'говядина', 'сосиски', 'мясо',"грудка", "шейка","свинина","ветчина",
             "рыба","окорочка","форель","хамон"],
    'хлеб': ['шоти', 'хлеб','лаваш',"ромашка","багет"],
    "яйца": ["яйца",],
    'п/фабрикаты': ['пельмени', 'хинкали', 'курица-гриль', "блинчики","блины"],
    'крупы': ['макароны','спагетти' ,'булгур','мука','рис', "паста", "лапша","горох","овсянка"],
    "др. продукты": ["Carrefour","Назилбе", "подсолнечное масло", "соус", "майонез", "сода","продукты"
                     "соль", "уксус", "томатная паста","специи", "аджика","арахис","кетчуп","огурчик"],
    'вкусняшки': ['печенье', 'Барни', 'шоколадка', 'сникерс', 'сушки', 'пироженка', 'булочка', 'гамбургер',"симит",
                  "пицца","M&Ms","конфеты","мед",'пирожок', 'хачапури', "пирожок", "мороженое", "жвачка", "чипсы","вафли","хот-дог", "круасан"],
    'напитки': ['сок', 'газировка', 'кола', 'компот', 'минералка','чай','кофе', "растворимый", "Борджоми","напиток",
                "мин.вода","бутилирован","спирт"],
    "животные": ["корм", "котята", "глистогон", "смесь", "паштет", "собак", "несквик", 'бентонит', "пеленки", "кошк",
                 "каниверм"],
    'алкоголь': ['пиво', 'шампанское', 'вино', 'чача', 'коньяк', 'целикаури', 'саперави', 'игристое вино',"консервы"],
    "бытовая химия":["зубная паста","зубщая щетка","порошок", "стиральный порошок", "мыло", "хозяйствен", "шампунь",                                                                                                          "жидкость для стирки",
    "бумага туалет", "стирки","фейри","гель"],
    'Уля':['театральная студия','театр','подготовка к школе','гимнастика', "канцелярия", "картон", "цветная","кукла",
               "альбом", "листы", "носки", "маркеры", "скотч","футболка", "мастер класс","Ульяна","занятия"],
    'связь': ['телефон', 'интернет', 'минуты', 'magti', 'silknet', "сотовый"],
    'коммуналка': ['газ', 'электричество', 'вода','коммуналка', "ситиком", "citycom","лифт"],
    "ремонт": ["гидроизоляция", "краска", "ключ","грунтовка","шкурка","гипсов","душ","клей","штапель","скотч брайт"],
    'кафе': ['кафе', 'Dona', 'Дона'],
    "аптека":["аптека", "бинт", "пластины","презерватив"],
    'транспорт':['проезд','такси', "автобус","транспорт","жд","билет"],
    "услуги": ['стрижка',"DHL","ремонт"]
}


import pandas as pd
import numpy as np

# создаю пустую таблицу для заполнения
Dic_df = pd.DataFrame(columns=['name', 'cat'])

# на основании категорий и товаров создаю таблицу для поиска по наименованию наподобие Redis
for key, value in Category.items():
    data = {key:value}
    df = pd.DataFrame({'name':value})
    df['cat'] = np.repeat(key, len(value))
    Dic_df = pd.concat([Dic_df, df], ignore_index=True)
Dic_df = Dic_df.sort_values(by='name')
Dic_df['id'] = range(1, len(Dic_df)+1)
Dic_df = Dic_df[["id",'name','cat']]
print(Dic_df)




