from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.shortcuts import redirect

from . import models
from profiles.models import User
# Create your views here.


class ListChatView(generic.TemplateView):
    template_name = "chat_app/list_chat.html"

class SendMessageView(generic.TemplateView):
    template_name = "chat_app/list_chat.html"

class ChatView(generic.TemplateView):
    template_name = "chat_app/list_chat.html"


class CreateChanelView(generic.View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        print(self.request.POST['id'])
        # target_user : User = User.objects.filter(pk=self.kwargs['pk'])
        # print('target user {}'.format(self.kwargs.get('pk')))
        # return redirect('chat_app:chanel_detail', args=(1,))
        return redirect('chat_app:chanel_detail')