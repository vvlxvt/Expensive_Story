from datetime import datetime, timedelta
import calendar

def get_month_range(month:str)->tuple:
    desired_year = datetime.now().year
    desired_month = list(calendar.month_abbr).index(month.capitalize())
    current_month = datetime.now().month
    if current_month < desired_month:
        desired_year -= 1
    start_date = datetime(desired_year, desired_month, 1)
    if desired_month == 12:
        end_date = start_date.replace(year=desired_year+1,month=1, day=31)
    else:
        end_date = start_date.replace(month=start_date.month % 12 + 1, day=1) - timedelta(days=1)
    return start_date, end_date

def get_week_range()->tuple:
    current_datetime = datetime.now().replace(second=0, microsecond=0)
    # Вычисляем начало текущей недели
    start_of_week = (current_datetime - timedelta(days=current_datetime.weekday())).date()
    return start_of_week, current_datetime

print(get_month_range('feb'))