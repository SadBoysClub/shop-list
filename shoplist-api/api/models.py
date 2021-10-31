from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.db.models.fields import CharField

# Create your models here.
class List(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE)
    code = CharField(max_length=8)
    creation_date = models.DateTimeField(auto_now_add=True)


class ListItem(models.Model):
    list_id = models.ForeignKey(List, on_delete=CASCADE)
    name = models.CharField(max_length=100)
    add_date = models.DateField(auto_now_add=True)
    added_by = models.ForeignKey(User)
    buy_date = models.DateField(blank=True, null=True)
    bought_by = models.ForeignKey(User)
    details = models.CharField(max_length=300)
    fiscal_note = models.ImageField()
