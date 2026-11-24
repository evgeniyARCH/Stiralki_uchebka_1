from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import json

class VkKeyboardUniversal:

    COLORS = {"BLUE": VkKeyboardColor.PRIMARY,
    "WHITE": VkKeyboardColor.SECONDARY,
    "RED": VkKeyboardColor.NEGATIVE,
    "GREEN": VkKeyboardColor.POSITIVE,
    }

    # Функция, которая возвращает пустую клавиатуру
    @staticmethod
    def return_empty_keyboard():
        vk_keyboard = VkKeyboard()
        return vk_keyboard.get_empty_keyboard()

    #Функция, которая добавляет блок кнопок определенного размера с параметрами из файла
    @staticmethod
    def add_defined_button_block(width, height, vk_keyboard): # buttons_dict (словарь, в котором будут все данные о конкретной кнопке: текст и цвет) ???
        # dict_keys = list(buttons_dict)
        # print(vk_keyboard.get_empty_keyboard())
        if json.loads(vk_keyboard.get_keyboard())['buttons'] != [[]]:
            print(0)
            vk_keyboard.add_line()
        for h in range(height):
            for w in range(width):
                # if len(dict_keys) < (h*width+w+1):
                #     return vk_keyboard
                text = 'gg'
                color = VkKeyboardUniversal.COLORS['RED']
                vk_keyboard.add_button(text, payload={'type': 'text'}, color=color) # По факту text и color будут браться из button_dict
            if h+1 < height: vk_keyboard.add_line()
        return vk_keyboard