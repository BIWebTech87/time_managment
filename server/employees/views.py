
from .models import Employee
from .forms import EmployeeLoginForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from .serializers import EmployeeSerializer
from django.contrib.auth.views import LoginView
from rest_framework.permissions import IsAuthenticated
from .perrmitions import IsAuthenticatedAndSuperuser
from rest_framework.response import Response
from rest_framework.views import APIView

@method_decorator(csrf_exempt, name='dispatch')
class EmployeeVeiwSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    http_method_names = ['get','post', 'put', 'patch']
    permission_classes = [IsAuthenticatedAndSuperuser]

@method_decorator(csrf_exempt, name='dispatch')
class EmployeeLoginView(LoginView):
    template_name = 'login.html'
    form_class = EmployeeLoginForm

    def get_form_kwargs(self):
        keyword = super().get_form_kwargs()
        keyword.pop('request', None)
        return keyword
