from sqlalchemy import create_engine, MetaData, Table, func
from sqlalchemy.orm import Session, registry, DeclarativeBase
from sqlalchemy.orm.exc import MultipleResultsFound
from database.expense import Expense
from services.aux_functions import get_month_range, get_week_range
from datetime import datetime


engine = create_engine('sqlite:///data/master.db')
# engine = create_engine(f'sqlite:///../data/sqlite_database.db')

# Создаём` объект MetaData
meta = MetaData()

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

def get_subname(item):
    try:
        stmt = session.query(DictTable.cat).filter_by(name = item).one_or_none()
    except MultipleResultsFound as e:
        print(f"MultipleResultsFound error: {e}")  # Дополнительный код для обработки ошибки
        stmt = session.query(DictTable.cat).filter_by(name=item).first()
    except Exception as e:
        print(f"Unexpected error: {e}")
    return stmt


def add_new_data(instance: Expense):  #
    new_data = MainTable()
    new_data.name = instance.name
    new_data.sub_name = instance.subname
    new_data.price = instance.price
    new_data.created = instance.today
    new_data.raw = instance.raw
    new_data.user_id = instance.user_id
    if instance.flag == True:
        set_value(instance.name, instance.subname)
    session.add(new_data)
    session.commit()
    session.close()

def del_last_note():
    '''ф. удаляет из базы данных или из БД и словаря, если было добавление в словарь'''
    table_last_id = session.query(func.max(MainTable.id)).scalar() # получаю id последней записи в таблице
    main_name_query = session.query(MainTable).filter(MainTable.id == table_last_id).scalar()
    main_name = main_name_query.name

    dict_last_id = session.query(func.max(DictTable.id)).scalar() # получаю id последней записи в словаре
    dict_name_query= session.query(DictTable).filter(DictTable.id == dict_last_id).scalar()
    dict_name = dict_name_query.name

    if dict_name == main_name:
        session.delete(main_name_query)
        session.delete(dict_name_query)
        print('удалил из словаря и БД')
    else:
        session.delete(main_name_query)
        print('удалил из БД')
    session.commit()
    session.close()
    return main_name

def format_output(res:list[tuple])->list[str]:
    # фильтрует пустые значения из запроса по категориям за месяц
    # преобразует список кортежей в список строк
    filtered_res = [(key, value) for key, value in res if value is not None]
    formatted_res = [f'{key}: {value}' for key, value in filtered_res]
    return formatted_res

def get_stat_month(mm: str):
    start_date, end_date = get_month_range(mm)
    result = session.query(MainTable.sub_name, func.round(func.sum(MainTable.price), 2))\
        .filter(MainTable.created >= start_date, MainTable.created <= end_date)\
        .group_by(MainTable.sub_name)\
        .order_by(func.sum(MainTable.price).desc()).all()
    return '\n'.join(format_output(result))

def get_stat_week():
    start_date, end_date = get_week_range()
    result = session.query(MainTable.sub_name, func.round(func.sum(MainTable.price), 2))\
        .filter(MainTable.created >= start_date, MainTable.created <= end_date)\
        .group_by(MainTable.sub_name)\
        .order_by(func.sum(MainTable.price).desc()).all()
    return '\n'.join(format_output(result))

def spend_today():
    start_date = datetime.today().date()
    end_date = datetime.now().replace(second=0, microsecond=0)
    result = session.query(func.round(func.sum(MainTable.price),2))\
            .filter(func.DATE(MainTable.created) >= start_date, func.DATE(MainTable.created) <= end_date).scalar()
    return result

def spend_week():
    start_date, end_date = get_week_range()
    result = session.query(func.sum(MainTable.price)).filter(func.DATE(MainTable.created) >= start_date,
                                                             func.DATE(MainTable.created) <= end_date).scalar()
    return result

def spend_month(month):
    start_date, end_date = get_month_range(month)
    result = session.query(func.round(func.sum(MainTable.price),2)).filter(func.DATE(MainTable.created) >= start_date,
                                                             func.DATE(MainTable.created) <= end_date).scalar()
    return result

def dict_upload(dict_categories: dict):
    with Session(engine) as session:
        for key, value in dict_categories.items():
            for elem in value:
                set_value(elem, key)
        session.commit()


def get_my_expenses(user_id):
    result = session.query(MainTable.name, func.round(MainTable.price,2))\
        .filter(MainTable.user_id == user_id)\
        .order_by(MainTable.created.desc())\
        .limit(10).all()
    return '\n'.join(format_output(result))