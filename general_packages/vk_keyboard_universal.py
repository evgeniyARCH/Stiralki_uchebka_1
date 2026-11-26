from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import json

class VkKeyboardUniversal:

    COLORS = {
        "BLUE": VkKeyboardColor.PRIMARY,
        "WHITE": VkKeyboardColor.SECONDARY,
        "RED": VkKeyboardColor.NEGATIVE,
        "GREEN": VkKeyboardColor.POSITIVE,
    }

    # Функция, которая проверяет клавиатуру на пустоту, а так же может сразу её активировать. Если activate = True, то функция возвращает клавиатуру!!!
    @staticmethod
    def check_keyboard_for_empty(vk_keyboard, activate = False):
        if json.loads(vk_keyboard.get_keyboard())['buttons'] == [[]]:
            if activate: return vk_keyboard.get_empty_keyboard()
            return True
        else:
            if activate: return vk_keyboard.get_keyboard()
            return False

    #Функция, которая добавляет блок кнопок определенного размера с параметрами из файла Button_data = словарь определенного блока клавиатуры
    @staticmethod
    def add_button_block(buttons_data, vk_keyboard):
        if not VkKeyboardUniversal.check_keyboard_for_empty(vk_keyboard=vk_keyboard):
            vk_keyboard.add_line()

        for i in range(len(buttons_data["Text"])):
            if (i) % buttons_data["Width"] == 0 and i != 0:
                vk_keyboard.add_line()
            text = buttons_data["Text"][i]
            color = VkKeyboardUniversal.COLORS[buttons_data["Color"]]
            vk_keyboard.add_button(text, payload={'type': 'text'}, color=color)
        return vk_keyboard  

    