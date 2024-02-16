from re import template
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class SpotterRegisterView(generic.FormView):
    template = 'user/registration.html'
    form_class = UserCreationForm
    redirect_authenticated_user =True
    successful_url = reverse_lazy('home')


class SpotterLoginView(LoginView):
    template_name = 'user/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')
