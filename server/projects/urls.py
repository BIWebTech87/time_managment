# projects/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import ProjectViewSet, TaskViewSet
from .views import ProjectsListView, ProjectCreateView, ProjectUpdateView, TaskListView, TaskCreateView, TaskUpdateView

# Create a router for API endpoints
router = DefaultRouter()
router.register(r'api/projects', ProjectViewSet)
router.register(r'api/tasks', TaskViewSet)

app_name = 'projects'

urlpatterns = [
    # Include the API endpoints from the router
    path('', include(router.urls)),
    
    # Your existing URL patterns
    path('projects_list/', ProjectsListView.as_view(), name='projects_list'),
    path('add_new_project/', ProjectCreateView.as_view(), name='add_new_project'),
    path('<int:pk>/', ProjectUpdateView.as_view(), name='edit_project'),
    # tasks
    path('tasks_list/', TaskListView.as_view(), name='tasks_list'),
    path('add_new_task/', TaskCreateView.as_view(), name='add_new_task'),
    path('task/<int:pk>/', TaskUpdateView.as_view(), name='edit_task'),
]