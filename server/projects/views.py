from .models import Project
from rest_framework.viewsets import ModelViewSet
from .serializers import ProjectSerializer


# Create your views here.
class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    print(queryset)


