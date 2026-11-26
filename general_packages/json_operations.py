class JsonOperations:
    # Функция, проверяющая работающие машинки
    @staticmethod
    def check_work_machines(settings_data, buttons_data):
        machines_data = list(settings_data["Стиралки"]["Машинки"])
        _text = []
        for i in range(len(machines_data)):
            if settings_data["Стиралки"]["Машинки"][machines_data[i]] == "Работает":
                _text.append(machines_data[i])
        buttons_data["washing_machine_select_buttons"]["Text"] = _text
        return buttons_data