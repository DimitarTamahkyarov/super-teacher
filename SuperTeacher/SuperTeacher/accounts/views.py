from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from SuperTeacher.accounts.forms import UserForm


class UserRegisterView(CreateView):
    form_class = UserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')


class ProfileView(DetailView):
    template_name = 'accounts/profile.html'
    context_object_name = 'user'
