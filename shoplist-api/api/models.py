from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.contrib.auth.models import GroupManager, User
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _

# Create your models here.
class List(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE)
    code = CharField(max_length=8)
    creation_date = models.DateTimeField(auto_now_add=True)


class ListItem(models.Model):
    list_id = models.ForeignKey(List, on_delete=CASCADE)
    name = models.CharField(max_length=100)
    add_date = models.DateField(auto_now_add=True)
    added_by = models.ForeignKey(
        User, on_delete=SET_NULL, null=True, related_name="added_by"
    )
    buy_date = models.DateField(blank=True, null=True)
    bought_by = models.ForeignKey(
        User, on_delete=SET_NULL, null=True, related_name="bought_by"
    )
    details = models.CharField(max_length=300)
    quantity = models.IntegerField()

    class MeasureUnit(models.TextChoices):
        GRAM = "g", _("gram")
        MILLILITER = "ml", _("milliliter")
        UNIT = "u", _("unit")


    quantity_measure = models.CharField(
        choices=MeasureUnit.choices, default=MeasureUnit.UNIT, max_length=2
    )
    fiscal_note = models.ImageField()
