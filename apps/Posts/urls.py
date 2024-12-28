from django.urls import path
from apps.Posts import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'posts'
urlpatterns = [
    path('',views.PostListView.as_view(), name="list"),
    path('create/',views.PostCreateView.as_view(), name="create"),
    path('<slug>/',views.PostDetailView.as_view(), name="detail"),
    path('<slug>/updated/',views.PostUpdateView.as_view(), name="updated"),
    path('<slug>/delete/',views.PostDeleteView.as_view(), name="delete"),
    path('like/<slug>/', views.like, name='like'),

    #base
    path('base',views.Base, name="base")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
