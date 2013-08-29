 
from myfirstapp.models import Poll
from django.contrib import admin
from myfirstapp.models import Choice

admin.site.register(Poll)
admin.site.register(Choice)