from django.urls import path
from apps.authentication import views
app_name = 'authentication'

urlpatterns = [
    path('login/', views.LoginView, name='accountslogin'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
