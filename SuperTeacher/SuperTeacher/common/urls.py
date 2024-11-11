from django.urls import path
from SuperTeacher.common.views import index, DashboardView, share_functionality, comment_functionality

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard' ),
    path('share/<int:profile_id>/', share_functionality, name='share'),
    path('comment/<int:profile_id>/', comment_functionality, name='comment')
]