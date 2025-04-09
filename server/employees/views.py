from django.core.checks import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.views import View
from .models import Employee
from .forms import EmployeeDataForm, NewEmployeeForm, DeleteEmployeeForm, EmployeeLoginForm
from rest_framework import viewsets
from .serializers import EmployeeSerializer
from django.contrib.auth.views import LoginView
from rest_framework.permissions import IsAuthenticated
from .perrmitions import IsAuthenticatedAndSuperuser


class EmployeeVeiwSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    http_method_names = ['get','post', 'put', 'patch']
    permission_classes = [IsAuthenticatedAndSuperuser]


class EmployeeLoginView(LoginView):
    template_name = 'login.html'
    form_class = EmployeeLoginForm

    def get_form_kwargs(self):
        keyword = super().get_form_kwargs()
        keyword.pop('request', None)
        return keyword