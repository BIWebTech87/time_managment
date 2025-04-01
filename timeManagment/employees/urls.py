from django.urls import path
from django.contrib.auth import views as auth_views
from .views import EmployeesList

app_name = 'employees'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('employees_list/', EmployeesList.as_view() , name='employees_list'),
]
