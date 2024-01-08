from datetime import datetime, timedelta
import calendar

def has_passed_month(reference_month):
    # возвращает true если месяц уже прошел с текущей даты
    current_date = datetime.now()
    last_month = current_date - timedelta(days=current_date.day)
    return last_month.month > reference_month
def get_month_range(month:str)->tuple:
    # получаем даты начала и конца запрашиваемого месяца
    year = datetime.now().year
    month_num = list(calendar.month_abbr).index(month.capitalize())
    if has_passed_month(month_num):
        year-= 1 # получаем текущий год
    if month_num == 12:
        end_date = datetime(year + 1, 1, 1) - timedelta(days=1)
    else:
        end_date = datetime(year, month_num+1, 1) - timedelta(days=1)
    start_date = datetime(year, month_num, 1)
    # Определение конца месяца путем перехода к следующему месяцу и вычитания одного дня
    print('месяц', start_date, end_date, sep = ' ')
    return start_date, end_date

def get_week_range()->tuple:
    current_datetime = datetime.now()
    # Вычисляем начало текущей недели
    start_of_week = current_datetime - timedelta(days=current_datetime.weekday())
    return start_of_week, current_datetime


