from general_packages.processing_days_and_times import ProcessingDays, ProcessingTime
from general_packages.generation_and_delete_days import GenerationAndDeleteDays
import json
import os

with open("settings.json", "r", encoding="utf-8") as f:
    f_data = json.load(f)

add_delta = f_data["Стиралки"]["Параметры"]["Количество дней"]
delete_delta = f_data["Стиралки"]["Параметры"]["Количество резервных дней"]
path = f_data["Папки"]["Папка с днями"]

# date = ProcessingTime.get_current_date()

# days = os.listdir(path)
# day = '22 ноября 2026'
# time_start = ProcessingTime.convert_str_to_datetime('12:00')
# time_finish = ProcessingTime.convert_str_to_datetime('18:00')

# GenerationAndDeleteDays.add_day(current_day=date, delta=add_delta, path=path)
# GenerationAndDeleteDays.delete_day(current_day=date, delta=delete_delta, path=path)
# print(ProcessingDays.sort_days(path))


# Стиралка 1
# days = os.listdir(path)
day = '22 ноября 2026'
time_start = ProcessingTime.convert_str_to_datetime('16:00')
time_finish = ProcessingTime.convert_str_to_datetime('18:00')
allowed_time = f_data["Стиралки"]["Ограничения"]["Максимальное время на одну запись (в часах)"]
delta = 0
if ProcessingTime.possibility_choose_start_time(path=path, day=day, time=time_start, mode="1-я: стиралка", delta=delta):
    print(ProcessingTime.possibility_choose_finish_time(path=path, day=day, time_start=time_start, time_finish=time_finish, allowed_time=allowed_time, mode="1-я: стиралка", delta=delta))