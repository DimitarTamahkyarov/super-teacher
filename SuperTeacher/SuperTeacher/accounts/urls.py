from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from SuperTeacher.accounts.views import UserRegisterView, ProfileView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', include([
        path('', ProfileView.as_view(), name='profile'),
        # path('edit/', views.edit_profile, name='profile-edit'),
        # path('delete/', views.delete_profile, name='profile-delete'),
    ]))
]