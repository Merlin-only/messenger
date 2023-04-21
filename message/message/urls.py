"""
URL configuration for message project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('default/', views.default, name='default'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/chats/', views.ChatList.as_view(), name='chat-list'),
    path('api/v1/chats/<int:pk>/', views.ChatDetail.as_view(), name='chat-detail'),
    path('api/v1/chats/<int:chat_id>/members/', views.RoomMemberList.as_view(), name='member-list'),
    path('api/v1/chats/<int:chat_id>/members/<int:pk>/', views.RoomMemberDetail.as_view(), name='member-detail'),
    path('api/v1/chats/<int:chat_id>/messages/', views.MessageList.as_view(), name='message-list'),
    path('api/v1/chats/<int:chat_id>/messages/<int:pk>/', views.MessageDetail.as_view(), name='message-detail'),
    path('api/v1/users/', views.UserList.as_view(), name='user-list'),
    path('api/v1/users/<int:user_id>/', views.UserMessageView.as_view(), name='user-message'),
    path('api/v1/profile/', views.UserProfileView.as_view(), name='user-profile'),
    path('ws/chat/<int:chat_id>/', views.ChatConsumer.as_asgi()),
]

