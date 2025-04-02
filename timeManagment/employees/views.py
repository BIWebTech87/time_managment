from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views import View
from .models import Employee
from .forms import EmployeeDataForm, NewEmployeeForm
from django.http import HttpResponse,JsonResponse

# Create your views here.
class EmployeesCRUD(View):
    model = Employee
    template_name = 'employees_template.html'

    def get(self, request, *args, **kwargs):
        context = {
            'title':'Employees',
        }

        try:
            employee = get_object_or_404(Employee, pk=kwargs.get('pk'))
        except Http404:
            context['error_employee_does_not_exist'] = f"Employee with pk:{kwargs.get('pk')} Does not Exist"
            return render(request, self.template_name, context)


        if get_object_or_404(Employee, pk=kwargs.get('pk')):
            employee = get_object_or_404(Employee, pk=kwargs.get('pk'))

            form = EmployeeDataForm(instance=employee)
            context = {
                'employee' : employee,
                'title' : employee,
                'form' : form,
            }
            return render(request, 'employees_template.html', context)
        else:
            context['error_employee_does_not_exist'] = 'Employees'
            context['form'] = NewEmployeeForm()
            context['employees_list'] = Employee.objects.all().order_by('id')
            context['total_employees'] = context['employees_list'].count()
        return render(request, self.template_name , context)
