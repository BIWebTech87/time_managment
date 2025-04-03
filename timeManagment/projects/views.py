from django.shortcuts import render
from .models import Project
from django.views import View


# Create your views here.
class ProjectsListView(View):
    model = Project
    template_name = 'projects_template.html'

    def get(self, request):
        context = {
            'title':'Projects',
            'project_list': Project.objects.all().order_by('id'),
            'total_projects': Project.objects.all().count(),
        }

        return render(request, self.template_name , context)