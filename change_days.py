from general_packages.processing_days_and_times import ProcessingDays, ProcessingTime
from general_packages.generation_and_delete_days import GenerationAndDeleteDays
import json
from time import sleep

with open("settings.json", "r", encoding="utf-8") as f:
    f_data = json.load(f)

uchebka_add_delta = f_data["Учебка"]["Параметры"]["Количество дней"]
stiralki_add_delta = f_data["Стиралки"]["Параметры"]["Количество дней"]
delete_delta = f_data["Стиралки"]["Параметры"]["Количество резервных дней"]

path = f_data["Папки"]["Папка с днями"]

while True:
    date = ProcessingTime.get_current_date()
    if ProcessingTime.convert_datetime_to_str(date) == '00:01':
        GenerationAndDeleteDays.add_day(current_day=date, delta=max([stiralki_add_delta, uchebka_add_delta]), path=path)
        GenerationAndDeleteDays.delete_day(current_day=date, delta=delete_delta, path=path)

    sleep(5)