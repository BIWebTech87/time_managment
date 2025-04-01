from django.shortcuts import render
from django.views import View
from .models import Employee
from django.http import HttpResponse,JsonResponse

# Create your views here.
class EmployeesList(View):
    model = Employee

    def get(self, request, *args, **kwargs):
        context = {
            'title':'Employees list',
            'employees_list':Employee.objects.all().order_by('id'),
            'total_employees': Employee.objects.count()
        }
        return render(request, 'employees_list.html', context)