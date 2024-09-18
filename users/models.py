from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True)
    groups = models.ManyToManyField('auth.Group', related_name='users', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='users', blank=True)

