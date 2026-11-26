from general_packages.processing_days_and_times import ProcessingTime
import os
import datetime
import json

class CheckInput:
    # Функция, которая показывает, можно ли начать запись с этого времени
    @staticmethod
    def interval_possibility_choose_start_time(path, day, time, mode, delta=0):
        # mode - стиралки/учебка. delta - Минимальное время записи (только для учебки). time идет в виде объекта datetime, день в строчном формате
        if os.path.exists(f'{path}/{day}.json'):
            with open(f"{path}/{day}.json", "r", encoding="utf-8") as f:
                f_data = json.load(f)

            times_dict = f_data[mode]
            times_dict_keys = list(times_dict)
            for i in range(len(times_dict_keys)):
                times_dict_keys_i_list = times_dict_keys[i].split(' - ')
                time_start = ProcessingTime.convert_str_to_datetime(times_dict_keys_i_list[0])
                time_finish = times_dict_keys_i_list[1]
                if ProcessingTime.convert_datetime_to_str(time_start - datetime.timedelta(minutes=delta)) <= ProcessingTime.convert_datetime_to_str(time) < time_finish:
                    return False
            return True
        return False

    # Функция, которая показывает, можно ли закончить запись с этим временем
    @staticmethod
    def interval_possibility_choose_finish_time(path, day, time_start, time_finish, allowed_time, mode, delta=0):
        # mode - стиралки/учебка. delta - Минимальное время записи (только для учебки). time идет в виде объекта datetime, день в строчном формате
        if os.path.exists(f'{path}/{day}.json'):
            with open(f"{path}/{day}.json", "r", encoding="utf-8") as f:
                f_data = json.load(f)

            times_dict = f_data[mode]
            times_dict_keys = list(times_dict)
            if ProcessingTime.convert_datetime_to_str(time_start) < ProcessingTime.convert_datetime_to_str(time_finish) and ProcessingTime.convert_datetime_to_str(time_start+datetime.timedelta(hours=allowed_time)) >= ProcessingTime.convert_datetime_to_str(time_finish):
                for i in range(len(times_dict_keys)):
                    times_dict_keys_i_list = times_dict_keys[i].split(' - ')
                    _time_start = times_dict_keys_i_list[0]
                    _time_finish = ProcessingTime.convert_str_to_datetime(times_dict_keys_i_list[1])
                    if _time_start < ProcessingTime.convert_datetime_to_str(time_finish) <= ProcessingTime.convert_datetime_to_str(_time_finish + datetime.timedelta(minutes=delta)):
                        return False
                    if ProcessingTime.convert_datetime_to_str(time_start) < _time_start < ProcessingTime.convert_datetime_to_str(time_finish):
                        return False
            else: 
                return False
                
            return True
        return False
    