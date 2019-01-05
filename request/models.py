from django.contrib.auth.models import AbstractUser as baseUser
from django.db import models


# Create your models here.


class MyUser(baseUser):
    access_token = models.CharField(max_length=255, null=True, blank=True)
    refresh_token = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username
