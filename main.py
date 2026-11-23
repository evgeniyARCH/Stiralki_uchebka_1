from general_packages.processing_days_and_times import ProcessingDays, ProcessingTime
from general_packages.generation_and_delete_days import GenerationAndDeleteDays
import json
import os

with open("settings.json", "r", encoding="utf-8") as f:
    f_data = json.load(f)

add_delta = f_data["Стиралки"]["Параметры"]["Количество дней"]
delete_delta = f_data["Стиралки"]["Параметры"]["Количество резервных дней"]
path = f_data["Папки"]["Папка с днями"]

date = ProcessingTime.get_current_date()

days = os.listdir(path)

# GenerationAndDeleteDays.add_day(current_day=date, delta=add_delta, path=path)
# GenerationAndDeleteDays.delete_day(current_day=date, delta=delete_delta, path=path)
print(ProcessingDays.sort_days(path))