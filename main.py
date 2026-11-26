import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

from general_packages.vk_bot import VkBot

import json

with open("./settings.json", "r", encoding="utf-8") as f:
    settings_data = json.load(f)

TOKEN = settings_data["Общие"]["token"]

vk = vk_api.VkApi(token=TOKEN)
longpoll = VkLongPoll(vk)

for event in longpoll.listen():
    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:

            # Сообщение от пользователя

            request = event.text
            user_id = event.user_id

            with open("./settings.json", "r", encoding="utf-8") as f:
                settings_data = json.load(f)

            with open("./buttons.json", "r", encoding="utf-8") as f:
                buttons_data = json.load(f)

            bot = VkBot(user_id=user_id, request=request, settings_data=settings_data, buttons_data=buttons_data)
            bot.custom_button(buttons_data=buttons_data["dates_buttons"])
            bot.custom_button(buttons_data=buttons_data["back_button"])
            # bot.custom_button(width=1, height=2)
            message, keyboard = bot.return_message_and_keyboard()

            vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': get_random_id(), 'keyboard': keyboard})
    


