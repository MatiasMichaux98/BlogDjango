from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Post, Like
from .forms import PostForm, CommentForm
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
class PostListView(ListView):
    model= Post
    context_object_name = 'post'

class PostDetailView(DetailView):
    model = Post

    def post(self, *args, **kwargs):
        form = CommentForm(self.request.POST)
        if form.is_valid():
            post = self.get_object()
            comment = form.instance
            comment.user = self.request.user
            comment.post = post
            comment.save()
            return redirect('detail', slug=post.slug)
        return self.get(self, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form': CommentForm()
        })
        return context

class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post

class PostCreateView(CreateView):
    form_class = PostForm
    model = Post

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'

def like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like = Like.objects.filter(user=request.user,post=post)
    if like.exists():
        like[0].delete()
        return redirect('detail',slug)
    Like.objects.create(user=request.user, post=post)
    return redirect('detail', slug)

def Base(request):
    return render(request, 'base/base.html')