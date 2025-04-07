from importlib.metadata import requires

from rest_framework import serializers

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'email', 'password', 'first_name', 'last_name']  # Exclude `groups`, unless needed
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        employee = Employee.objects.create_user(**validated_data)
        return employee
