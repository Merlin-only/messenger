from rest_framework import serializers
from .models import Chat, Message, UserProfile
from django.contrib.auth.models import User


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'


class GroupChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'name']


class MessageSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    recipient_username = serializers.CharField(write_only=True)

    class Meta:
        model = Message
        fields = ['id', 'chat', 'author', 'content', 'timestamp', 'recipient_username']


class GroupMessageSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Message
        fields = ['id', 'chat', 'author', 'content', 'timestamp']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'avatar']


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile']
