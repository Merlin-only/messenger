import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'chat'
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_type = data['type']

        if message_type == 'create_chat':
            # Обработка создания чата

        elif message_type == 'delete_chat':
            # Обработка удаления чата

        elif message_type == 'update_profile':
            # Обработка обновления профиля

        elif message_type == 'get_messages':
            # Обработка получения сообщений

        elif message_type == 'send_message':
            # Обработка отправки сообщения

        elif message_type == 'get_user_list':
            # Обработка получения списка пользователей
