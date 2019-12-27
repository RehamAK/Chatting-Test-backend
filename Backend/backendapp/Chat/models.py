from django.db import models
from django.utils import timezone




class ChatRoom(models.Model):

    fromUser = models.CharField(max_length=200)
    toUser = models.CharField(max_length=200)
    created = models.DateTimeField(default=timezone.now)


class ChatMessage(models.Model):

    Message = models.CharField(max_length=200)
    created = models.DateTimeField(default=timezone.now)
    RoomID = models.OneToOneField(ChatRoom, on_delete=models.CASCADE, related_name="Messages")


