import django_tables2
from .models import ChanelData


class ChanelDataTable(django_tables2.Table):

    chat_detail = django_tables2.TemplateColumn(template_name='chat_app/table/chat_detail.html')

    class Meta:
        model = ChanelData
        fields = ['pk', 'other_user',]
        template_name = 'django_tables2/bootstrap.html'
