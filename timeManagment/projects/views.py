from django.shortcuts import render
from .models import Project
from django.views import View
from .forms import NewProjectForm
from django.shortcuts import redirect

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
    
    
class ProjectCreateView(View):
    model = Project
    template_name = 'projects_template.html'

    def get(self, request):
        form = NewProjectForm()
        context = {
            'title': 'Create new project',
            'form': form,
            'form_title': "Create new project",
            "form_button": "Create"
        }
        return render(request, self.template_name, context)

    def post(self, request):
        context = {
            'title': 'Create new project',
        }
        form = NewProjectForm(request.POST)
        if form.is_valid():
            new_project=form.save()
            return redirect('projects:projects_list')
        else:
            context['form'] = form
            context['form_title'] = "Create new project"
            context['form_button'] = "Create"
            context['error_msg'] = "Form is not valid"
        return render(request, self.template_name, context)