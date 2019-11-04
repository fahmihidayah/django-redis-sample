from django.urls import path, include
from .views import ListChatView

app_name = 'chat_app'

urlpatterns = (
    path('list_chat', ListChatView.as_view(), name='list_chat'),
)