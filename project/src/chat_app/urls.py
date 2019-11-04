from django.urls import path, include
from . import views

app_name = 'chat_app'

urlpatterns = (
    path('list_chat', views.ListChatView.as_view(), name='list_chat'),
    path('chanel_detail/<int:pk>', views.ChatView.as_view(), name='chanel_detail'),
    path('create_chanel/<int:pk>', views.CreateChanelView.as_view(), name='create_chanel'),
    path('send_message/<int:pk>', views.SendMessageView.as_view(), name='send_message'),
)