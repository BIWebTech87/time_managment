from django.forms import ModelForm
from .models import Project,Task
from django import forms


class NewProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control"}),
            'description': forms.Textarea(attrs={'class': "form-control"}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'is_active': forms.CheckboxInput(attrs={'class': "form-check-input"}),
            'created_at': forms.DateTimeInput(attrs={'type': 'date', 'class': "form-control"}),
            'updated_at': forms.DateTimeInput(attrs={'type': 'date', 'class': "form-control"}),
            'client': forms.TextInput(attrs={'class': "form-control"}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'manager': forms.Select(attrs={'class': 'form-control'}),
            'team_members': forms.SelectMultiple(attrs={'class': 'form-control', 'size': '5'}),
        }


class NewTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            'project',
            'title',
            'description',
            'assigned_to',
            'status',
            'priority',
            'redline',
        ]
        widgets = {
            'project': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': "form-control"}),
            'description': forms.Textarea(attrs={'class': "form-control"}),
            'assigned_to': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'redline': forms.DateInput(attrs={'type': 'date'}),
        }



class UpdateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'project': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': "form-control"}),
            'description': forms.Textarea(attrs={'class': "form-control"}),
            'assigned_to': forms.Select(attrs={'class': 'form-control'}),
            'initial_time': forms.DateTimeInput(attrs={'type': 'datetime-local',}),
            'final_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'redline': forms.DateInput(attrs={'type': 'date'}),
        }
