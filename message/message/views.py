from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Chat, Message, RoomMember, UserProfile
from .serializers import ChatSerializer, MessageSerializer, RoomMemberSerializer, UserSerializer, UserProfileSerializer
from django.shortcuts import render
from django.contrib.flatpages.models import FlatPage
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class ChatList(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class ChatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]


class RoomMemberList(generics.ListCreateAPIView):
    serializer_class = RoomMemberSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        chat_id = self.kwargs['chat_id']
        return RoomMember.objects.filter(chat__id=chat_id)

    def perform_create(self, serializer):
        chat_id = self.kwargs['chat_id']
        chat = Chat.objects.get(id=chat_id)
        serializer.save(user=self.request.user, chat=chat)


class RoomMemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoomMember.objects.all()
    serializer_class = RoomMemberSerializer
    permission_classes = [IsAuthenticated]


class MessageList(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        chat_id = self.kwargs['chat_id']
        return Message.objects.filter(chat__id=chat_id)

    def perform_create(self, serializer):
        chat_id = self.kwargs['chat_id']
        chat = Chat.objects.get(id=chat_id)
        serializer.save(author=self.request.user, chat=chat)
        self.send_message(chat_id, serializer.data)

    def send_message(self, chat_id, message_data):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f'chat_{chat_id}',
            {
                'type': 'chat_message',
                'message': message_data
            }
        )


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_profile = request.user.user_profile
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)

    def patch(self, request):
        user_profile = request.user.user_profile
        serializer = UserProfileSerializer(user_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user_profile = request.user.user_profile
        user_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def home(request):
    flatpage = FlatPage.objects.get(url='/home/')
    return render(request, 'flatpages/home.html', {'flatpage': flatpage})


def default(request):
    return render(request, 'flatpages/default.html')
