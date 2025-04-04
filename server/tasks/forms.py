from .models import Task
from django import forms


class NewTaskForm(forms.ModelForm):
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
