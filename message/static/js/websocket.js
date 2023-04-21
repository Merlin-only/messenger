var chatSocket = new WebSocket('ws://' + window.location.host + '/ws/chat/');

chatSocket.onmessage = function(event) {
    var data = JSON.parse(event.data);
    var messageType = data['type'];

    if (messageType === 'create_chat') {
        console.log('Chat created successfully');
    } else if (messageType === 'delete_chat') {
        console.log('Chat deleted successfully');
    } else if (messageType === 'update_profile') {
        console.log('Profile updated successfully');
    } else if (messageType === 'get_messages') {
        // Обновление отображения сообщений
    } else if (messageType === 'send_message') {
        console.log('Message sent successfully');
    } else if (messageType === 'get_user_list') {
        $('#user-list').html(data['html']);
    }
};

function createChat(name, users) {
    var data = {
        'type': 'create_chat',
        'name': name,
        'users': users
    };
    chatSocket.send(JSON.stringify(data));
}

function deleteChat(chatId) {
    var data = {
        'type': 'delete_chat',
        'chatId': chatId
    };
    chatSocket.send(JSON.stringify(data));
}

function editProfile(formData) {
    var data = {
        'type': 'update_profile',
        'formData': formData
    };
    chatSocket.send(JSON.stringify(data));
}

function getMessages(chatId) {
    var data = {
        'type': 'get_messages',
        'chatId': chatId
    };
    chatSocket.send(JSON.stringify(data));
}

function sendMessage(chatId, content) {
    var data = {
        'type': 'send_message',
        'chatId': chatId,
        'content': content
    };
    chatSocket.send(JSON.stringify(data));
}

function getUserList() {
    var data = {
        'type': 'get_user_list'
    };
    chatSocket.send(JSON.stringify(data));
}
