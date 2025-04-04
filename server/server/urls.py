from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('api/v1/', include('employees.urls', namespace='employees')),
    path('api/v1/project/', include('projects.urls', namespace='projects')),
]
