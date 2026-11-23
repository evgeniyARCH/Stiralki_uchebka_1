import datetime
import os

class ProcessingDays:
    CONVERT_DATETIME_TO_STR_DICT = {
        '01': 'января',
        '02': 'февраля',
        '03': 'марта',
        '04': 'апреля',
        '05': 'мая',
        '06': 'июня',
        '07': 'июля',
        '08': 'августа',
        '09': 'сентября',
        '10': 'октября',
        '11': 'ноября',
        '12': 'декабря'
    }

    CONVERT_STR_TO_DATETIME_DICT = {
        'января': "01",
        'февраля': "02",
        'марта': "03",
        'апреля': "04",
        'мая': "05",
        'июня': "06",
        'июля': "07",
        'августа': "08",
        'сентября': "09",
        'октября': "10",
        'ноября': "11",
        'декабря': "12"
        }

    # Функция для конвертации строчной даты (09 марта 2027) в объект datetime
    @staticmethod
    def convert_str_to_datetime(date):
        _date_list = date.strip().split(' ')
        _day = _date_list[0]
        _month = ProcessingDays.CONVERT_STR_TO_DATETIME_DICT[_date_list[1].lower()]
        _year = _date_list[2]
        _date = f'{_day}.{_month}.{_year}'
        return datetime.datetime.strptime(_date, '%d.%m.%Y')

    # Функция для конвертации объекта datetime в строчную дату (09 марта 2027)
    @staticmethod
    def convert_datetime_to_str(date):
        _day = date.strftime('%d')
        _month = ProcessingDays.CONVERT_DATETIME_TO_STR_DICT[date.strftime('%m')]
        _year = date.strftime('%Y')
        _date = f'{_day} {_month} {_year}'
        return _date

    # Функция, которая возвращает в формате datetime день, который получится прибавлением (убавлением) определенного количества дней относительно исходной даты
    @staticmethod
    def calculation_day(date, delta):
        return date + datetime.timedelta(days=delta)

    # Функиця для сортировки дней в порядке возрастания. Так же она сразу выгружает файлы-дни
    @staticmethod
    def sort_days(path):
        days_list_files = os.listdir(path)
        days_list = []
        for y in range(len(days_list_files)):
            days_list.append(days_list_files[y].split('.')[0])

        days_list_datetime = {}
        for i in range (len(days_list)):
            key = ProcessingDays.convert_str_to_datetime(days_list[i])
            days_list_datetime[key] = days_list[i]

        sort_days_list = []
        keys = list(days_list_datetime)
        for s in range(len(keys)):
            min_day = days_list_datetime[min(keys)]
            del keys[keys.index(min(keys))]
            sort_days_list.append(min_day)
        return sort_days_list



    def __str__():
        return f'Класс обрабоки даты'


class ProcessingTime:
    # Функция, которая возвращает текущее время и день в формате datetime
    @staticmethod
    def get_current_date():
        return datetime.datetime.now()

    # Функция для конвертации строчного времени (09:00) в объект datetime
    @staticmethod
    def convert_str_to_datetime(time):
        return datetime.datetime.strptime(time, '%H:%M')

    # Функция для конвертации объекта datetime в строчное время (09:00)
    @staticmethod
    def convert_datetime_to_str(time):
        return time.strftime('%H:%M')

    def __str__():
        return f'Класс обрабоки времени'