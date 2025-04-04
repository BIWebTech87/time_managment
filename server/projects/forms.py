from django.forms import ModelForm
from .models import Project
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