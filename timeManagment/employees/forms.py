from django.forms import ModelForm
from employees.models import Employee

class EmployeeLoginForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['username', 'password']
