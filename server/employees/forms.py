from django.forms import ModelForm,Form
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
            'password',
            'role',
            'is_superuser',
            'is_staff',
            'is_active',
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
            'is_superuser'
        ]

class DeleteEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = [
            'email',
        ]