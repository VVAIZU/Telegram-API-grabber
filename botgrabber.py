from telethon.sync import TelegramClient, events
from telethon import functions

api_id = ''
api_hash = ''
#phone_number = ''

# Каналы, из которых будут браться новые посты
source_channel_ids = []

# Канал, в который будут пересылаться новые посты
forward_channel_id = 

# Создание экземпляра клиента TelegramClient
client = TelegramClient('sessionA', api_id, api_hash, system_version='4.16.30-vxCUSTOM', device_model='your_device_model', app_version='your_app_version')

# Запуск клиента
with client:
    # Обработка новых постов в каналах
    @client.on(events.NewMessage(chats=source_channel_ids))
    async def forward_posts(event):
        # Получение информации о посте
        message = event.message

        # Пересылка поста на канал -1001844013839 с кнопкой "Отправить"
        forwarded_message = await client.forward_messages(-1xxxxxxx, message)
        # Создание кнопки "Отправить"
        button_data = f'send_message_{forwarded_message.id}'
        # Отправка сообщения без кнопок
        #await client.send_message(-1001844013839, 'Пересланное сообщение:\n\nОтправить')

    # Обработка нажатий на кнопку
    @client.on(events.CallbackQuery(pattern=r'send_message_(\d+)'))
    async def send_message(event):
        message_id = int(event.pattern_match.group(1))
        message = await event.client.get_messages(-1xxxxxxx, ids=message_id)

        # Проверка, содержит ли сообщение фотографию
        if message.photo:
            # Если сообщение содержит фотографию, пересылка без подписи
            await client.forward_messages(forward_channel_id, message.photo)
        else:
            # Если сообщение не содержит фотографию, пересылка текстового сообщения без подписи
            await client.send_message(forward_channel_id, message.text)

    # Запуск клиента в режиме ожидания событий
    client.run_until_disconnected()
