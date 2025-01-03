from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Post, Like
from .forms import PostForm, CommentForm
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.db.models import Q



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
            return redirect('posts:detail', slug=post.slug)
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

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context.update({
            "view_type":"updated"
        })
        return context

class PostCreateView(CreateView):
    form_class = PostForm
    model = Post
    success_url = reverse_lazy('posts:list')

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context.update({
            "view_type":"create"
        })
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'

def like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like = Like.objects.filter(user=request.user,post=post)
    if like.exists():
        like[0].delete()
        return redirect('posts:detail',slug)
    Like.objects.create(user=request.user, post=post)
    return redirect('posts:detail', slug=slug)


class SearchPost(ListView):
    model = Post

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            object_list = Post.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
        else:
            object_list = Post.objects.none()
        return object_list