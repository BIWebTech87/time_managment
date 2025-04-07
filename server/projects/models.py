from django.db import models
from employees.models import Employee

# Create your models here.
class Project(models.Model):
    name = models.CharField()
    description = models.TextField()
    client = models.CharField()
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(choices=[
        ('in_preparation', 'In Preparation'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('on_hold', 'On Hold'),
    ],
        default='in_preparation'
    )
    priority = models.CharField(choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ],
        default='low'
    )
    is_active = models.BooleanField(default=True)
    manager = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='managed_projects')
    team_members = models.ManyToManyField(Employee, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name