from general_packages.processing_days_and_times import ProcessingDays, ProcessingTime
from general_packages.generation_and_delete_days import GenerationAndDeleteDays
from general_packages.json_operations import JsonOperations
import json
import os

with open("settings.json", "r", encoding="utf-8") as f:
    f_data = json.load(f)

add_delta = f_data["Учебка"]["Параметры"]["Количество дней"]
delete_delta = f_data["Учебка"]["Параметры"]["Количество резервных дней"]
path = f_data["Папки"]["Папка с днями"]

date = ProcessingTime.get_current_date()

# days = os.listdir(path)
# day = '22 ноября 2026'
# time_start = ProcessingTime.convert_str_to_datetime('12:00')
# time_finish = ProcessingTime.convert_str_to_datetime('18:00')

# GenerationAndDeleteDays.add_day(current_day=date, delta=add_delta, path=path)
# GenerationAndDeleteDays.delete_day(current_day=date, delta=delete_delta, path=path)
# print(ProcessingDays.sort_days(path))

with open("./settings.json", "r", encoding="utf-8") as f:
    settings_data = json.load(f)

with open("./buttons.json", "r", encoding="utf-8") as f:
    buttons_data = json.load(f)

buttons_data = JsonOperations.check_work_machines(settings_data=settings_data, buttons_data=buttons_data)
with open("buttons.json", "w", encoding="utf-8") as f:
    json.dump(buttons_data, f, ensure_ascii=False, indent=4)  # indent=4 делает JSON более читаемым с отступами
