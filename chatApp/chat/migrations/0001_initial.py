# Generated by Django 4.2.2 on 2023-06-30 09:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('date', models.DateTimeField(default=datetime.datetime(2023, 6, 30, 9, 44, 58, 260464))),
                ('room', models.CharField(max_length=1000)),
                ('content', models.CharField(max_length=1000000)),
            ],
        ),
        migrations.CreateModel(
            name='room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
    ]
