from django.db import models
from datetime import datetime

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=1000)

class Message(models.Model):
    user = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.now, blank= True)
    room = models.CharField(max_length=1000)
    content = models.CharField(max_length=1000000)
