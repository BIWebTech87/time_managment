from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('api/v1/employees/', include('employees.urls', namespace='employees')),
    path('api/v1/projects/', include('projects.urls', namespace='projects')),
    path('api/v1/tasks/', include('tasks.urls', namespace='tasks')),
)
