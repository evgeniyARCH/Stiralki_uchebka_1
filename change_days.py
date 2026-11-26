from general_packages.processing_days_and_times import ProcessingDays, ProcessingTime
from general_packages.generation_and_delete_days import GenerationAndDeleteDays
import json
from time import sleep

with open("settings.json", "r", encoding="utf-8") as f:
    settings_data = json.load(f)

with open("buttons.json", "r", encoding="utf-8") as f:
    buttons_data = json.load(f)

uchebka_add_delta = settings_data["Учебка"]["Параметры"]["Количество дней"]
stiralki_add_delta = settings_data["Стиралки"]["Параметры"]["Количество дней"]
stiralki_delete_delta = settings_data["Стиралки"]["Параметры"]["Количество резервных дней"]
uchebka_delete_delta = settings_data["Учебка"]["Параметры"]["Количество резервных дней"]

path = settings_data["Папки"]["Папка с днями"]

buttons_data["dates_buttons"]["Text"] = ProcessingDays.return_visible_days(days_list=ProcessingDays.sort_days(path=path), settings_data=settings_data)
with open("buttons.json", "w", encoding="utf-8") as f:
    json.dump(buttons_data, f, ensure_ascii=False, indent=4)  # indent=4 делает JSON более читаемым с отступами

while True:
    date = ProcessingTime.get_current_date()
    if ProcessingTime.convert_datetime_to_str(date) == '18:36':
        GenerationAndDeleteDays.add_day(current_day=date, delta=max([stiralki_add_delta, uchebka_add_delta]), path=path)
        GenerationAndDeleteDays.delete_day(current_day=date, delta=max([stiralki_delete_delta, uchebka_delete_delta]), path=path)

    sleep(5)