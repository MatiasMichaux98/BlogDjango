from django.db import models
from apps.authentication.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to="image",default="iconoPerfil.jpg",null=True,blank=True)
    full_name = models.CharField(max_length=100,null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self) :
        return self.user.username
    
    def save(self, *args, **kwargs):
        if not self.full_name:
            self.full_name = self.user.username
        super().save(*args, **kwargs)

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
