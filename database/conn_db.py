from sqlalchemy import create_engine, MetaData, Table, inspect, func
from sqlalchemy.orm import Session, registry, DeclarativeBase
from sqlalchemy.orm.exc import MultipleResultsFound
from database.expense import Expense
from services.aux_functions import get_month_range, get_week_range
from datetime import datetime

# Создаем объект Engine, представляющий базу данных SQLite3
# engine = create_engine('sqlite:///C:/Users/vital/PycharmProjects/Expensive_Story/database/new.db')
engine = create_engine('sqlite:////data/new.db')

# Создаём` объект MetaData
meta = MetaData()

# Используем inspect для проверки наличия таблицы
inspector = inspect(engine)

# Создаю объект registry
mapper_registry = registry()

# Получаю объекты Table
main_table = Table('main', meta, autoload_with=engine)
dict_table = Table('category', meta, autoload_with=engine)

class MainTable:
    pass

class DictTable:
    pass

mapper_registry.map_imperatively(MainTable, main_table)
mapper_registry.map_imperatively(DictTable, dict_table)
# установить соответствие (маппинг) между ORM-классом MyTable
# и существующей таблицей table в базе данных

class Base(DeclarativeBase):
    pass

# class Dict(Base):
#     __tablename__ = "category"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(30))
#     cat: Mapped[str] = mapped_column(String(30))

Base.metadata.create_all(bind=engine)

# Создаём` сессию для работы с базой данных
session = Session(engine)

def set_value(value, key):
     prod = DictTable(
         name = value,
         cat = key,
     )
     session.add(prod)
     session.commit()
     session.close()

def get_subname(elem):
    try:
        stmt = session.query(DictTable.cat).filter_by(name = elem).one_or_none()
    except MultipleResultsFound as e:
        print(f"MultipleResultsFound error: {e}")  # Дополнительный код для обработки ошибки
        stmt = session.query(DictTable.cat).filter_by(name=elem).first()
    except Exception as e:
        print(f"Unexpected error: {e}")
    print('get_subname', stmt)
    return stmt


def add_new_data(instance: Expense):  #
    new_data = MainTable()
    new_data.name = instance.name
    new_data.sub_name = instance.subname
    new_data.price = instance.price
    new_data.created = instance.today
    new_data.raw = instance.raw
    if instance.flag == True:
        set_value(instance.name, instance.subname)
    session.add(new_data)
    session.commit()
    session.close()

def del_last_note():

    table_last_id = session.query(func.max(MainTable.id)).scalar() # полцчаю id последней записи
    main_name_query = session.query(MainTable).filter(MainTable.id == table_last_id).scalar()
    main_name = main_name_query.name

    dict_last_id = session.query(func.max(DictTable.id)).scalar()
    dict_name_query= session.query(DictTable).filter(DictTable.id == dict_last_id).scalar()
    dict_name = dict_name_query.name

    if dict_name == main_name:
        session.delete(main_name_query)
        session.delete(dict_name_query)
        print('удалил оба')
    else:
        session.delete(main_name_query)
        print('удалил один')
    session.commit()
    session.close()
    return main_name


# def del_last_note():
#     max_id = session.query(func.max(MainTable.id)).scalar()
#     result_to_delete = session.query(MainTable).filter(MainTable.id == max_id).first()
#     if result_to_delete:
#         session.delete(result_to_delete)
#         session.commit()
#         session.close()
#         print(type(result_to_delete))
#         return result_to_delete.raw
#     else:
#         return 'нечего удалять'

def format_output(res:list[tuple])->list[str]:
    # фильтрует пустые значения из запроса по категоиям за месяц
    # преобразует список кортежей в список строк
    filtered_res = [(key, value) for key, value in res if value is not None]
    formatted_res = [f'{key}: {value}' for key, value in filtered_res]
    return formatted_res

def get_stat_month(mm: str):
    start_date, end_date = get_month_range(mm)
    result = session.query(MainTable.sub_name,
                           func.sum(MainTable.price))\
        .filter(MainTable.created >= start_date, MainTable.created <= end_date)\
        .group_by(MainTable.sub_name)\
        .order_by(func.sum(MainTable.price).desc()).all()
    return '\n'.join(format_output(result))

def get_stat_week():
    start_date, end_date = get_week_range()
    result = session.query(MainTable.sub_name,
                           func.sum(MainTable.price))\
        .filter(MainTable.created >= start_date, MainTable.created <= end_date)\
        .group_by(MainTable.sub_name)\
        .order_by(func.sum(MainTable.price).desc()).all()
    return '\n'.join(format_output(result))

def spend_today():
    today = datetime.today().date()
    result = session.query(func.sum(MainTable.price))\
        .filter(func.DATE(MainTable.created) == today).scalar()
    return result

def spend_week():
    start_date, end_date = get_week_range()
    result = session.query(func.sum(MainTable.price)).filter(func.DATE(MainTable.created) >= start_date,
                                                             func.DATE(MainTable.created) <= end_date).scalar()
    return result


def dict_upload(dict_categories: dict):
    with Session(engine) as session:
        for key, value in dict_categories.items():
            for elem in value:
                set_value(elem, key)
        session.commit()


