from django.db import models
from apps.authentication.models import User
from django.shortcuts import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    image = models.ImageField(upload_to='imagePost')
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("posts:detail",kwargs={
            "slug": self.slug
        })
    def get_like_url(self):
        return reverse("posts:like",kwargs={
            "slug": self.slug
        })
    
    @property
    def get_like_count(self):
        return self.like_set.all().count()
    @property
    def comments(self):
        return self.comment_set.all()
    @property
    def get_comment_count(self):
        return self.comment_set.all().count()
    
    
class comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    