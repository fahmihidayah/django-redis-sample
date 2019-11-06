from django.shortcuts import render
from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404
from django_tables2 import SingleTableView
from . import models
from profiles.models import User
from .tables import ChanelDataTable
# Create your views here.


class ListChatView(LoginRequiredMixin, SingleTableView):
    template_name = "chat_app/list_chat.html"
    model = models.ChanelData
    paginate_by = 10
    table_class = ChanelDataTable

    def get_queryset(self):
        chanel_data_query_set = models.ChanelData.objects.filter(models.models.Q(users__exact=self.request.user))
        return chanel_data_query_set.annotate(other_user=models.models.Subquery(User.objects.filter(
            ~models.models.Q(email=self.request.user.email)).values('email')))


class SendMessageView(LoginRequiredMixin, generic.TemplateView):
    template_name = "chat_app/list_chat.html"


class ChatView(LoginRequiredMixin, generic.TemplateView):
    template_name = "chat_app/chat.html"


    def get(self, request, *args, **kwargs):

        return super(ChatView, self).get(request, *args, **kwargs)


class CreateChanelView(LoginRequiredMixin, generic.View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        other_user: User = get_object_or_404(User, pk=self.request.POST['id'])
        current_user: User = self.request.user
        ids = [other_user.pk, current_user.pk]
        chanel_query = models.ChanelData.objects.annotate(
            count_related_user=models.models.Count('users', filter=models.models.Q(users__id__in=ids))
        ).filter(count_related_user=len(ids))

        if chanel_query.count() == 0:
            chanel: models.ChanelData = models.ChanelData()
            chanel.save()
            chanel.users.add(current_user, other_user)
            chanel.save()
        else:
            chanel: models.ChanelData = chanel_query.get()

        return redirect('chat_app:chanel_detail', pk=chanel.pk)