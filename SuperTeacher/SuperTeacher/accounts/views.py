from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from SuperTeacher.accounts.forms import AppUserCreationForm, StudentProfileEditForm, TeacherProfileEditForm
from SuperTeacher.accounts.models import StudentProfile, TeacherProfile
from SuperTeacher.accounts.utils import get_user_profile

UserModel = get_user_model()

class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)

        return response


class AppUserLoginView(LoginView):
    template_name = 'accounts/login.html'


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserModel
    template_name = 'accounts/profile-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        photos_with_likes = self.object.photo_set.annotate(likes_count=Count('like'))

        context['total_likes_count'] = sum(photo.likes_count for photo in photos_with_likes)
        context['total_photos_count'] = self.object.photo_set.count()

        return context


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'accounts/profile-edit.html'

    def get_object(self, queryset=None):
        profile = get_user_profile(self.request.user)
        return profile

    def get_form_class(self):
        profile = self.get_object()

        if isinstance(profile, TeacherProfile):
            return TeacherProfileEditForm
        elif isinstance(profile, StudentProfile):
            return StudentProfileEditForm
        else:
            raise ValueError("User has no valid profile type (Teacher or Student).")

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={
                'pk': self.object.pk,
            }
        )

class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'accounts/profile-delete.html'
    success_url = reverse_lazy('login')

    def get_object(self, queryset=None):
        profile = get_user_profile(self.request.user)
        return profile

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user