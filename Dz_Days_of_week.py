#1. Сегодня вторник, 13-е декабря 2022 года
#Используя только эту информацию вычислить день недели нового года.
#Подсказка: правильный ответ: воскресенье

#2. Есть ли годы, начинающиеся с пн? со вт?
#Привести ближайший пример.

#3. В какой день недели Вы родились? Перечислить все свои ДР,
#пришедшиеся на тот же день недели.

from datetime import datetime, date, time
import time
from datetime import timedelta



class Year:
    def __init__(self, year, month, day):
        self.__year = year
        self.__month = month
        self.__day = day

    def year_now(self):
        date_now = datetime.now()
        year_now = date_now.year
        return year_now

    def create_date(self):
        days = self.__day
        months = self.__month
        years = self.__year
        date_created = date(self.__year, self.__month, self.__day)
        return date_created

    def leap_year(self):
        import_year_from_year_now_method = self.year_now()
        days_for_this_year = 0
        if import_year_from_year_now_method % 4 ==0 and import_year_from_year_now_method % 100 ==0 and import_year_from_year_now_method % 400 ==0:
            days_for_this_year = 366
        else:
            days_for_this_year = 365
        return days_for_this_year

    def day_of_week_now(self):
        what_day = ""
        day_week = datetime.today().isoweekday()
        if day_week == 1:
            what_day = "Понедельник"
        elif day_week == 2:
            what_day = "Вторник"
        elif day_week == 3:
            what_day = "Среда"
        elif day_week == 4:
            what_day = "Четверг"
        elif day_week == 5:
            what_day = "Пятница"
        elif day_week == 6:
            what_day == "Суббота"
        else:
            what_day = "Воскресенье"
        return what_day

    def day_week(self):
        label_day = ""
        import_date_from_date_create = self.create_date()
        date_week = import_date_from_date_create.isoweekday()

        if date_week == 1:
            label_day = "Понедельник"
        elif date_week == 2:
            label_day = "Вторник"
        elif date_week == 3:
            label_day = "Среда"
        elif date_week == 4:
            label_day = "Четверг"
        elif date_week == 5:
            label_day = "Пятница"
        elif date_week == 6:
            label_day = "Суббота"
        else:
            label_day = "Воскресенье"
        return label_day

    def new_year_is_monday(self):
        get_name_day = self.day_week()
        get_year = self.__year
        get_month = self.__month
        get_day = self.__day

        result_day = ""
        if get_day == 1 and get_month == 1:
            if get_name_day == "Понедельник":
                result_day = "Понедельник"
            elif get_name_day == "Вторник":
                result_day = "Вторник"
            else:
                result_day = get_name_day
        # return f'{get_day}-{get_month}-{get_year} {result_day}'
        return result_day


print('--------Новые годы--------')
print()

day_new_year2023 = Year(2023, 1, 1)
day_new_year2024 = Year(2024, 1, 1)
print(f'Новый год {day_new_year2023.create_date()} это: {day_new_year2023.day_week()}')
print(f'Новый год {day_new_year2024.create_date()} это: {day_new_year2024.day_week()}')

print()
print('---------Дни рождения------')
print()

day_bith_day2020 = Year(2020, 9, 27)
day_bith_day2023 = Year(2023, 9, 27)
print(f'Ваш день рождения {day_bith_day2020.create_date()} это: {day_bith_day2020.day_week()}')
print(f'Ваш день рождения {day_bith_day2023.create_date()} это: {day_bith_day2023.day_week()}')

print()
print('---------Новые годы понедельник---------')
print()

if_new_year_is_monday2023 = Year(2023, 1, 1)
if_new_year_is_monday2024 = Year(2024, 1, 1)
if_new_year_is_monday2030 = Year(2030, 1, 1)
if_new_year_is_monday2029 = Year(2029, 1, 1)
if_new_year_is_monday2035 = Year(2035, 1, 1)
if_new_year_is_monday2036 = Year(2036, 1, 1)

print(f'Новый год {if_new_year_is_monday2023.create_date()} это {if_new_year_is_monday2023.new_year_is_monday()}')
print(f'Новый год {if_new_year_is_monday2024.create_date()} это {if_new_year_is_monday2024.new_year_is_monday()}')
print(f'Новый год {if_new_year_is_monday2030.create_date()} это {if_new_year_is_monday2030.new_year_is_monday()}')
print(f'Новый год {if_new_year_is_monday2029.create_date()} это {if_new_year_is_monday2029.new_year_is_monday()}')
print(f'Новый год {if_new_year_is_monday2035.create_date()} это {if_new_year_is_monday2035.new_year_is_monday()}')
print(f'Новый год {if_new_year_is_monday2036.create_date()} это {if_new_year_is_monday2036.new_year_is_monday()}')





