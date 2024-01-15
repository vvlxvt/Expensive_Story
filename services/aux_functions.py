from datetime import datetime, timedelta
import calendar

def has_passed_month(reference_month):
    # возвращает true если месяц этого года уже прошел с текущей даты
    year = datetime.now().year
    current_date = datetime.today()
    reference_date = datetime(year, reference_month, 1)
    print('запрашиваемый год', reference_date)
    return current_date > reference_date


def get_month_range(month:str)->tuple:
    # получаем даты начала и конца запрашиваемого месяца
    year = datetime.now().year
    month_num = list(calendar.month_abbr).index(month.capitalize())

def get_month_range(month: str) -> tuple:
    # получаем даты начала и конца запрашиваемого месяца
    desired_month = list(calendar.month_abbr).index(month.capitalize())
    desired_year = datetime.now().year  # Год текущей даты

    # Если указанный месяц текущего года еще не наступил, выбираем такой же месяц предыдущего года
    current_month = datetime.now().month
    if current_month < desired_month:
        desired_year -= 1

    # Вычисляем начало и конец периода месяца
    start_date = datetime(desired_year, desired_month, 1)
    end_date = start_date.replace(month=start_date.month % 12 + 1, day=1) - timedelta(days=1)
    return start_date, end_date

def get_week_range()->tuple:
    current_datetime = datetime.now().replace(second=0, microsecond=0)
    # Вычисляем начало текущей недели
    start_of_week = (current_datetime - timedelta(days=current_datetime.weekday())).date()
    return start_of_week, current_datetime

