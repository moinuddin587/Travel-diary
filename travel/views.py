from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Blog
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    return render(request, 'home.html')

def exit(request):
    return render(request, 'registration/logout.html')

class PostListView(ListView):
    model = Post
    template_name = 'posts.html'

class BlogListView(ListView):
    model = Blog
    template_name = 'blogs.html'
    
class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    
class BlogCreateView(LoginRequiredMixin,CreateView):
    model = Blog
    template_name = 'blog_new.html'
    fields = ['title', 'image', 'description']
    
    def form_valid(self, form):
       form.instance.author = self.request.user
       return super().form_valid(form)
    
class BlogUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Blog
    template_name = 'blog_edit.html'
    fields = ['title', 'image', 'description']
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
class BlogDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('post')
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user