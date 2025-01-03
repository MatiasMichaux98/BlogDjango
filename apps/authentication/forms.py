from django import forms
from .models import User

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']