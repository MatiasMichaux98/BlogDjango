from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
    def save(self ,*args, **kwargs):
        username_email = self.email.split('@')
        user = self.username
        if not self.full_name:
            self.full_name = user
        if not self.username:
            self.username = username_email
        super(User, self).save(*args ,**kwargs)

        