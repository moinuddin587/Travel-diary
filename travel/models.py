from django.db import models
from accounts.models import CustomUser
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    # author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blog_posts')
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images',default='default.jpg')
    description = models.TextField()
    tour_date = models.DateTimeField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    
    def __str__(self):
        return self.title
    
    

class Blog(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blog_posts')
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images',default='default.jpg')
    description = models.TextField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])