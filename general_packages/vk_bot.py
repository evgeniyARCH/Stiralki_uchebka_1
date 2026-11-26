from general_packages.vk_keyboard_universal import VkKeyboardUniversal
from vk_api.keyboard import VkKeyboard

class VkBot:
    def __init__(self, user_id, request, settings_data, buttons_data):
        self.user_id = user_id
        self.request = request

        self.vk_keyboard = VkKeyboard()
        self.buttons_data = buttons_data

        self.settings_data = settings_data
        self.message = settings_data["Общие"]["Ответ ошибка"]

    def custom_button(self, buttons_data): # Тестовая функция, пригодится в будущем
        self.vk_keyboard = VkKeyboardUniversal.add_button_block(buttons_data=buttons_data, vk_keyboard=self.vk_keyboard)

    def return_message_and_keyboard(self):
        return self.message, VkKeyboardUniversal.check_keyboard_for_empty(vk_keyboard=self.vk_keyboard, activate=True)

    def __str__():
        return f'Класс VkBot - главный самый!'
