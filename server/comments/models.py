from django.db import models
from employees.models import Employee
from tasks.models import Task
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
