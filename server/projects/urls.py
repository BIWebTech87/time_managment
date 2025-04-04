from django.urls import path, include
from rest_framework import routers
from projects.views import ProjectViewSet

app_name = 'projects'

project_routers = routers.DefaultRouter()
project_routers.register(r'projects', ProjectViewSet, basename='project')

urlpatterns = [
    path('', include(project_routers.urls)),
]
