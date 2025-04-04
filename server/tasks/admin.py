from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'assigned_to', 'priority')
    list_filter = ('status',)
    search_fields = ('title', 'description')

admin.site.register(Task, TaskAdmin)
