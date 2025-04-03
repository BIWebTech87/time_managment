from django.urls import path, include
from .views import ProjectsListView, ProjectCreateView

app_name = 'projects'

urlpatterns = [
    path('projects_list/', ProjectsListView.as_view(), name='projects_list'),
    path('add_new_project/', ProjectCreateView.as_view(), name='add_new_project')
    #path('<int:pk>/', EmployeeUpdateView.as_view(), name='edit_employee'),

]
