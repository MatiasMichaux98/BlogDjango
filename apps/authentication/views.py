from django.shortcuts import render
from django.contrib.auth import logout ,login, authenticate
from django.shortcuts import redirect
from django.contrib import messages
from .models import User

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import User

def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        
        # Verifica si las contraseñas coinciden
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("authentication:register")

        # Verifica si el nombre de usuario ya existe
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect("authentication:register")

        # Verifica si el correo electrónico ya está registrado
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect("authentication:register")

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            login(request, user)  
            return redirect("posts:list")
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect("authentication:register")
    
    return render(request, "signup.html")


def LoginView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('posts:list')
        else:
            messages.error(request, "Correo o contraseña no válidos")
            return redirect('authentication:accountslogin')

    return render(request, "login.html")

def logout_view(request):
    logout(request)