from django.shortcuts import render
from django.views import generic

# Create your views here.


class ListChatView(generic.TemplateView):
    template_name = "chat_app/list_chat.html"

