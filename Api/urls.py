from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v3/app/', include('events.urls', namespace='events')),
    path('api/v3/app/', include('nudges.urls', namespace='nudges')),
]
