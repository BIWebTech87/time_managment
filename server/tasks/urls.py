from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet

app_name = 'projects'

task_routers = routers.DefaultRouter()
task_routers.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(task_routers.urls)),
]
