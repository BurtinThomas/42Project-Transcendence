from django.contrib.auth.models import AbstractUser
from django.db import models

class GameUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False)
    username = models.CharField(max_length=150, unique=True, blank=False)
    password = models.CharField(max_length=128, blank=False)
    friends = models.ManyToManyField('GameUser', blank=True)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default_avatar.jpg', null=True, blank=True)
    online = models.BooleanField(default=False)

