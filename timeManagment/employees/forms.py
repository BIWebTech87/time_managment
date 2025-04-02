from django.forms import ModelForm
from employees.models import Employee

class EmployeeLoginForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['email', 'password']


class NewEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = [
            'first_name',
            'last_name',
            'email',
            'role',
            'is_staff',
            'is_active',
            'date_joined',
            'is_superuser'
        ]

class EmployeeDataForm(ModelForm):
    class Meta:
        model = Employee
        fields = [
            'first_name',
            'last_name',
            'email',
            'role',
            'is_staff',
            'is_active',
            'date_joined',
            'is_superuser'
        ]