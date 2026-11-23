import datetime
import os
from general_packages.processing_days_and_times import ProcessingDays

class GenerationAndDeleteDays:
    # Функция для удаления старого дня (только в стиралках). current_day - объект datetime
    @staticmethod
    def delete_day(current_day, delta, path):
        _date = current_day - datetime.timedelta(days=delta)
        _day = ProcessingDays.convert_datetime_to_str(_date)
        if os.path.exists(f'{path}/{_day}.json'):
            os.remove(f'{path}/{_day}.json')
            print(f'Удаление файла {path}/{_day}.json прошло успешно')

        for i in range(delta-1):
            _date = current_day - datetime.timedelta(days=i+1)
            _day = ProcessingDays.convert_datetime_to_str(_date)
            f = open(f'{path}/{_day}.json', 'a+', encoding='utf-8')
            f.close()
        print('Все файлы удаления восстановлены')

    # Функция для создания нового дня. current_day - объект datetime
    @staticmethod
    def add_day(current_day, delta, path):
        for i in range(delta):
            _date = current_day + datetime.timedelta(days=i)
            _day = ProcessingDays.convert_datetime_to_str(_date)
            f = open(f'{path}/{_day}.json', 'a+', encoding='utf-8')
            f.close()
        print('Все файлы создания восстановлены')