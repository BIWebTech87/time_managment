from django.shortcuts import render
from .models import Project, Task
from django.views import View
from .forms import NewProjectForm, NewTaskForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import Http404

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


class ProjectUpdateView(View):
    template_name = 'projects_template.html'

    def get_project(self, pk):
        """Утилитарный метод для получения сотрудника."""
        return get_object_or_404(Project, pk=pk)

    def get(self, request, *args, **kwargs):
        context = {'title': 'Project'}

        try:
            project = self.get_project(kwargs.get('pk'))
            form = NewProjectForm(instance=project)
            context.update({
                'title': project,
                'form': form,
                'form_title': "Update project data",
                "form_button": "Update",
            })
        except Http404:
            context['error_msg'] = f"Project with ID: {kwargs.get('pk')} doesn't exist"

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        project = self.get_project(kwargs.get('pk'))

        form = NewProjectForm(request.POST, instance=project)

        if form.is_valid():
            form.save()
            return redirect('projects:projects_list')

        context = {
            'title': project,
            'form': form,
            'form_title': "Update project data",
            'form_button': "Update",
        }
        return render(request, self.template_name, context)


class TaskListView(View):
    model = Task
    template_name = 'projects_template.html'

    def get(self, request):
        context = {
            'title': 'Tasks',
            'task_list': Task.objects.all().order_by('id'),
            'total_tasks': Project.objects.all().count(),
        }

        return render(request, self.template_name, context)


class TaskCreateView(View):
    model = Task
    template_name = 'projects_template.html'

    def get(self, request):
        form = NewTaskForm()
        context = {
            'title': 'Create new task',
            'form': form,
            'form_title': "Create new task",
            "form_button": "Create"
        }
        return render(request, self.template_name, context)

    def post(self, request):
        context = {
            'title': 'Create new task',
        }
        form = NewTaskForm(request.POST)
        if form.is_valid():
            new_task=form.save()
            return redirect('projects:tasks_list')
        else:
            context['form'] = form
            context['form_title'] = "Create new project"
            context['form_button'] = "Create"
            context['error_msg'] = "Form is not valid"
        return render(request, self.template_name, context)


class TaskUpdateView(View):
    template_name = 'employees_template.html'

    def get_task(self, pk):
        """Утилитарный метод для получения сотрудника."""
        return get_object_or_404(Task, pk=pk)

    def get(self, request, *args, **kwargs):
        context = {'title': 'Task'}

        try:
            task = self.get_task(kwargs.get('pk'))
            form = NewTaskForm(instance=task)
            context.update({
                'title': task,
                'form': form,
                'form_title': "Update Task data",
                "form_button": "Update",
            })
        except Http404:
            context['error_msg'] = f"Task with ID: {kwargs.get('pk')} doesn't exist"

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        project = self.get_task(kwargs.get('pk'))

        form = NewTaskForm(request.POST, instance=Task)

        if form.is_valid():
            form.save()
            return redirect('projects:task_list')

        context = {
            'title': Task,
            'form': form,
            'form_title': "Update task data",
            'form_button': "Update",
        }
        return render(request, self.template_name, context)