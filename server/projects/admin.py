from django.contrib import admin

from .models import Project


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'client', 'status', 'priority', 'is_active', 'manager')

admin.site.register(Project, ProjectAdmin)
