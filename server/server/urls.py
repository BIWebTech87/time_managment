# server/server/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('employee/', include('employees.urls', namespace='employees')),
    path('projects/', include('projects.urls', namespace='projects')),  # Changed to plural
]