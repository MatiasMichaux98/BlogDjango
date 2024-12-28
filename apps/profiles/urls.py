from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'profile'

urlpatterns = [
    path('', views.ProfileUpdateView.as_view(), name='profile'),  # Vista de actualización del perfil
    path('detail/', views.ProfileDetail.as_view(), name='profileDetail'),  # Vista de detalles del perfil
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
