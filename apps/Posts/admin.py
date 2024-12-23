from django.contrib import admin

# Register your models here.
from .models import Like, comment, Post

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(comment)