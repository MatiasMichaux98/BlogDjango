from django.shortcuts import  get_object_or_404 
from django.views.generic import UpdateView ,DetailView , ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import Profile
from apps.Posts.models import Post
@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ['image', 'full_name', 'bio']
    success_url = reverse_lazy('profile:profile')
    template_name = 'Profile.html'
    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user)
    
@method_decorator(login_required, name='dispatch')

class ProfileDetail(DetailView):
    model: Profile
    template_name = 'profileDetail.html'

    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Publicaciones'] = Post.objects.filter(user=self.request.user)
        return context

 