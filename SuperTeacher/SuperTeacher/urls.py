


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('SuperTeacher.common.urls')),
    path('accounts/', include('SuperTeacher.accounts.urls')),
    # path('reservations/', include('SuperTeacher.reservations.urls')),
    # path('photos/', include('SuperTeacher.photos.urls')),
]
