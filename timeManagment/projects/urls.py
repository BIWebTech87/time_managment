from django.urls import path, include
from .views import ProjectsListView, ProjectCreateView, ProjectUpdateView,TaskListView,TaskCreateView, TaskUpdateView

app_name = 'projects'

urlpatterns = [
    path('projects_list/', ProjectsListView.as_view(), name='projects_list'),
    path('add_new_project/', ProjectCreateView.as_view(), name='add_new_project'),
    path('<int:pk>/', ProjectUpdateView.as_view(), name='edit_project'),
    #tasks
    path('tasks_list/', TaskListView.as_view(), name='tasks_list'),
    path('add_new_task/', TaskCreateView.as_view(), name='add_new_task'),
    path('task/<int:pk>/', TaskUpdateView.as_view(), name='edit_task'),

]
