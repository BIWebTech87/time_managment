from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Task
from .serializers import TaskSerializer
from employees.perrmitions import IsAuthenticatedAndSuperuser


# Create your views here.
class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    http_method_names = ['get', 'put', 'post','patch']
    permision_classes = [IsAuthenticatedAndSuperuser]