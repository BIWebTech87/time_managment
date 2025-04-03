from django.urls import path, include
from .views import ProjectsListView

app_name = 'projects'

urlpatterns = [
    path('projects_list/', ProjectsListView.as_view(), name='projects_list'),
    #path('<int:pk>/', EmployeeUpdateView.as_view(), name='edit_employee'),
    #path('add_new_employee/', EmployeeCreateView.as_view(), name='add_new_employee')
]
