from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
import random
import time

vk = vk_api.VkApi(token="77868bc24de4414f7deb7f743bad4241b33d01610ef1787cdf84aeb4aecb23f2a31fb4fe8c4e36ab56797")

vk._auth_token()

vk.get_api()

longpoll = VkBotLongPoll(vk, 187159289)

while True:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.object.peer_id != event.object.from_id:
                if event.object.text.lower() == "привет":
                    vk.method("messages.send", {"peer_id": event.object.peer_id, "message": 'Привет, я бот на python что бы узнать мои команды пиши: Python , что бы узнать команды игрового бота пиши: помощь',
                                                "random_id": 0})
            elif event.object.peer_id == event.object.from_id:
                if event.object.text.lower() == "привет":
                    vk.method("messages.send", {"user_id": event.object.from_id, "message": 'Привет, я бот на python что бы узнать мои команды пиши: Python , что бы узнать команды игрового бота пиши: помощь',
                                            "random_id": 0})
            elif event.object.peer_id == event.object.from_id:
                if event.object.text.lower() == "python":
                    vk.method("messages.send", {"peer_id": event.object.from_id, "message": 'В разработке',
                                                "random_id": 0})
            elif event.object.peer_id != event.object.from_id:
                if event.object.text.lower() == "python":
                    vk.method("messages.send", {"user_id": event.object.peer_id, "message": 'В разработке',
                                                "random_id": 0})