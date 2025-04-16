# projects/serializers.py
from rest_framework import serializers
from .models import Project, Task
from employees.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'email', 'role']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    assigned_to_details = EmployeeSerializer(source='assigned_to', read_only=True)
    
    class Meta:
        model = Task
        fields = '__all__'