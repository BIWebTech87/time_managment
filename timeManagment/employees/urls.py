from django.urls import path
from django.contrib.auth import views as auth_views
from .views import EmployeesListView, EmployeeUpdateView, EmployeeCreateView

app_name = 'employees'


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('employees_list/', EmployeesListView.as_view() , name='employees_list'),
    path('<int:pk>/', EmployeeUpdateView.as_view() , name='edit_employee'),
    path('add_new_employee/', EmployeeCreateView.as_view() , name='add_new_employee'),
]
