from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('user_type', 'first_name', 'last_name', 'profile_image', 'email')