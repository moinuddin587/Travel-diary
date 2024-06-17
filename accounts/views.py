from django.shortcuts import render
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.views import generic
from django.urls import reverse_lazy

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
