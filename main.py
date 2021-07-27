import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from config import tok

vk_session = vk_api.VkApi(token = tok)
longpoll = VkBotLongPoll(vk_session, 205488261)

def sender(id, text):
    vk_session.method('messages.send', {'chat_id': id, 'message': text, 'random_id': 0})

def get_fullname(from_id):
    info = vk_session.method('users.get', {'user_ids': from_id})[0]
    full_name = info.get('first_name') + ' ' + info['last_name']
    return full_name

# Слушаем Long Poll
for event in longpoll.listen():
    # Если пришло сообщение
    if event.type == VkBotEventType.MESSAGE_NEW:
        #Если написали в беседу
        if event.from_chat:

            id = event.chat_id
            msg = event.object.message['text'].lower()

            try:
                act = event.message.action['type']
                invite_id = event.message.action['member_id']
            except:
                act = ''
                invite_id = -100

            if act == 'chat_invite_user':
                name = get_fullname(invite_id)
                sender(id, f'К нам присоединился [id{invite_id}|{name}], хаю-хай! &#128516;\n\n&#128214 Список команд Балабобы:\n&#9989 Балабоба, команды\n　　・Узнать список команд\n&#9989 Балабоба, как дела\n　　・Узнать работоспособность\n&#9989 Балабоба, (любой текст)　　・Набалабобить нейротекст без стиля\n&#9989 Балабоба (стиль), (любой текст)\n　　・Набалабобить нейротекст в указанном стиле.\n\n&#127912; Стили:\n0・Без стиля\n1・Теории заговора\n2・ТВ-репортажи\n3・Тосты\n4・Пацанские цитаты\n5・Рекламные слоганы\n6・Короткие истории\n7・Подписи в Instagram\n8・Википедия\n9・Синопсисы фильмов\n10・Гороскоп\n11・Народные мудрости\n12・Произведения современного искусства')

            if msg == 'балабоба, команды' || msg == 'балабоба команды' || msg == 'балабоба' || msg == 'балабиба':
                sender(id, '&#128214 Список команд Балабобы:\n&#9989 Балабоба, команды\n　　・Узнать список команд\n&#9989 Балабоба, как дела\n　　・Узнать работоспособность\n&#9989 Балабоба, (любой текст)　　・Набалабобить нейротекст без стиля\n&#9989 Балабоба (стиль), (любой текст)\n　　・Набалабобить нейротекст в указанном стиле.\n\n&#127912; Стили:\n0・Без стиля\n1・Теории заговора\n2・ТВ-репортажи\n3・Тосты\n4・Пацанские цитаты\n5・Рекламные слоганы\n6・Короткие истории\n7・Подписи в Instagram\n8・Википедия\n9・Синопсисы фильмов\n10・Гороскоп\n11・Народные мудрости\n12・Произведения современного искусства')
            else if msg == 'балабоба, как дела?' || msg == 'балабоба как дела?' || msg == 'балабоба, как дела' || msg == 'балабоба как дела':
                sender(id, 'Как дела? Нормально! Нормально нереально!')
            else if msg == 'балабоба, привет!' || msg == 'балабоба привет!' || msg == 'балабоба, привет' || msg == 'балабоба привет':
                sender(id, 'Привет!')

# if event.text == 'Первый вариант фразы' or event.text == 'Второй вариант фразы': #Если написали заданную фразу
#     if event.from_user: #Если написали в ЛС
#         vk.messages.send( #Отправляем сообщение
#             user_id=event.user_id,
#             message='Ваш текст'
# )
#     elif event.from_chat: #Если написали в Беседе
#         vk.messages.send( #Отправляем собщение
#             chat_id=event.chat_id,
#             message='Ваш текст'
# )

# while True:
#     messages = vk.method("messages.getConversations", {"offset": 0, "count": 5, "filter": "unanswered"})
#     text = messages['items'][0]
#     print(text)
#     print()
#     print("=====================================================================================")
#     print()
#     time.sleep(10)
