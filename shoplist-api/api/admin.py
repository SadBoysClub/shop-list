from typing import List
from django.contrib import admin
from .models import ListItem, List

# Register your models here.

admin.site.register(List)
admin.site.register(ListItem)
