from django.urls import path
from .views import PostListView,BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('blogs/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='post-detail'),
    path('blog/new/', BlogCreateView.as_view(), name='blog_new' ),
    path('blog/update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
]