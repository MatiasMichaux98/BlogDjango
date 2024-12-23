from django import forms
from .models import Post , comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ('content', )