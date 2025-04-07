from .models import Project
from rest_framework.viewsets import ModelViewSet
from .serializers import ProjectSerializer
from employees.perrmitions import IsAuthenticatedAndSuperuser


# Create your views here.
class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permision_classes = [IsAuthenticatedAndSuperuser]
    http_method_names = ['get', 'put', 'patch']


