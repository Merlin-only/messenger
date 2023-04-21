const chatSocket = new WebSocket(
    'ws://' + window.location.host +
    '/ws/chat/' + chatId + '/');

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    switch (data.type) {
        case 'chat_message':
            // Обновление отображения сообщений
            break;
        case 'create_chat':
            // Обновление списка чатов
            break;
        case 'delete_chat':
            // Обновление списка чатов
            break;
        case 'edit_profile':
            // Обновление отображения профиля
            break;
        case 'user_list':
            // Обновление списка пользователей
            break;
        default:
            console.error('Unknown message type:', data.type);
            break;
    }
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

function createChat(name, users) {
    const data = {
        type: 'create_chat',
        name: name,
        users: users,
    };
    chatSocket.send(JSON.stringify(data));
}

function deleteChat(chatId) {
    const data = {
        type: 'delete_chat',
        chat_id: chatId,
    };
    chatSocket.send(JSON.stringify(data));
}

function editProfile(formData) {
    const data = {
        type: 'edit_profile',
        form_data: formData,
    };
    chatSocket.send(JSON.stringify(data));
}

function getMessages(chatId) {
    const data = {
        type: 'get_messages',
        chat_id: chatId,
    };
    chatSocket.send(JSON.stringify(data));
}

function sendMessage(chatId, content) {
    const data = {
        type: 'send_message',
        chat_id: chatId,
        content: content,
    };
    chatSocket.send(JSON.stringify(data));
}

function getUserList() {
    const data = {
        type: 'get_user_list',
    };
    chatSocket.send(JSON.stringify(data));
}
