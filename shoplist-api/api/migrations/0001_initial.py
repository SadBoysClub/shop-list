# Generated by Django 3.2.8 on 2021-10-31 22:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=8)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('add_date', models.DateField(auto_now_add=True)),
                ('buy_date', models.DateField(blank=True, null=True)),
                ('details', models.CharField(max_length=300)),
                ('quantity', models.IntegerField()),
                ('quantity_measure', models.CharField(choices=[('g', 'gram'), ('ml', 'milliliter'), ('u', 'unit')], default='u', max_length=2)),
                ('fiscal_note', models.ImageField(upload_to='')),
                ('added_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='added_by', to=settings.AUTH_USER_MODEL)),
                ('bought_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bought_by', to=settings.AUTH_USER_MODEL)),
                ('list_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.list')),
            ],
        ),
    ]