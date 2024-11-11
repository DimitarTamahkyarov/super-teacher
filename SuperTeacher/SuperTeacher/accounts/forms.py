from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from SuperTeacher.accounts.models import StudentProfile, TeacherProfile

UserModel = get_user_model()

class AppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email', 'is_teacher')

class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class TeacherProfileEditForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        exclude = ('user', 'rating')


class StudentProfileEditForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        exclude = ('user', )