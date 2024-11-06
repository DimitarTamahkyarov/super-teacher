from django.urls import path

from SuperTeacher.common.views import index

urlpatterns = [
    path('', index, name='index'),
]