import django_tables2 as tables
from .models import User


class UserTable(tables.Table):

    class Meta:
        model = User
        fields = ['id', 'email', 'name',]
        template_name = 'django_tables2/bootstrap.html'
