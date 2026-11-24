from general_packages.vk_keyboard_universal import VkKeyboardUniversal
from vk_api.keyboard import VkKeyboard

class VkBot:
    def __init__(self, user_id, request, f_data):
        self.user_id = user_id
        self.request = request

        self.vk_keyboard = VkKeyboard()
        self.keyboard = self.vk_keyboard.get_empty_keyboard()

        self.f_data = f_data
        self.message = f_data["Общие"]["Ответ ошибка"]

    def custom_button(self, width, height): # Тестовая функция, пригодится в будущем
        self.vk_keyboard = VkKeyboardUniversal.add_defined_button_block(width=width, height=height, vk_keyboard=self.vk_keyboard)
        self.keyboard = self.vk_keyboard.get_keyboard()

    def return_message_and_keyboard(self):
        return self.message, self.keyboard
