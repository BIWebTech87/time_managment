from django.core.checks import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.views import View
from .models import Employee
from .forms import EmployeeDataForm, NewEmployeeForm, DeleteEmployeeForm, EmployeeLoginForm
from rest_framework import viewsets
from .serializers import EmployeeSerializer
from django.contrib.auth.views import LoginView

class EmployeeVeiwSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    http_method_names = ['get', 'post', 'put', 'patch']


class EmployeeLoginView(LoginView):
    template_name = 'login.html'
    form_class = EmployeeLoginForm

    def get_form_kwargs(self):
        keyword = super().get_form_kwargs()
        keyword.pop('request', None)
        return keyword


'''class EmployeesListView(View):
    model = Employee
    template_name = 'employees_template.html'

    def get(self, request):

        context = {
            'title':'Employees',
            'employees_list': Employee.objects.all().order_by('id'),
            'total_employees': Employee.objects.all().count(),
        }

        return render(request, self.template_name , context)
'''

class EmployeeUpdateView(View):
    template_name = 'employees_template.html'

    def get_employee(self, pk):
        """Утилитарный метод для получения сотрудника."""
        return get_object_or_404(Employee, pk=pk)

    def get(self, request, *args, **kwargs):
        """Обрабатывает GET-запрос для отображения формы редактирования сотрудника."""
        context = {'title': 'Employees'}

        try:
            employee = self.get_employee(kwargs.get('pk'))
            form = EmployeeDataForm(instance=employee)
            form_fire = DeleteEmployeeForm()
            context.update({
                'title': employee,
                'form': form,
                'form_title': "Update employee data",
                "form_button": "Update",
                'form_fire': form_fire,
                'form_fire_button': 'Delete',
                'form_fire_title': "Fire employee(for fire a employee insert a email)",
                'form_fire_url': f'employees/{employee.id}/delete_employee/',
            })
        except Http404:
            context['error_msg'] = f"Employee with ID: {kwargs.get('pk')} doesn't exist"

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """Обрабатывает POST-запрос для разных форм."""
        action = request.POST.get('action')  # Получаем действие из скрытого поля
        employee = self.get_employee(kwargs.get('pk'))

        if action == 'update':
            # Основная форма (обновление данных сотрудника)

            form = EmployeeDataForm(request.POST, instance=employee)

            if form.is_valid():
                form.save()
                return redirect('employees:employees_list')  # Перенаправляем на список сотрудников

            # Если форма некорректна
            context = {
                'title': employee,
                'form': form,
                'form_title': "Update employee data",
                'form_button': "Update",
            }
            return render(request, self.template_name, context)

        elif action == 'delete':
            form = DeleteEmployeeForm(request.POST)
            if employee.email != form.data.get('email'):
                return render(request, self.template_name, {'error_msg': 'Email is not correct'})
            employee.delete()
            return redirect('employees:employees_list')  # Перенаправляем после удаления

        # Если "action" не распознано
        return redirect('employees:employees_list')


class EmployeeCreateView(View):
    model = Employee
    template_name = 'employees_template.html'

    def get(self, request):
        form = NewEmployeeForm()
        context = {
            'title': 'Create new employee',
            'form': form,
            'form_title': "Create new employee",
            "form_button": "Create"
        }
        return render(request, self.template_name, context)

    def post(self, request):
        context = {
            'title': 'Create new employee',
        }
        form = NewEmployeeForm(request.POST)
        if form.is_valid():
            new_employee=form.save(commit=False)
            new_employee.set_password(form.cleaned_data['password'])
            new_employee.save()
            return redirect('employees:employees_list')
        else:
            context['form'] = form
            context['form_title'] = "Create new employee"
            context['form_button'] = "Create"
            context['error_msg'] = "Form is not valid"
        return render(request, self.template_name, context)




