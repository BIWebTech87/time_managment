from django.contrib import admin
from .models import Employee
from django.contrib.auth.admin import UserAdmin

class EmployeeAdmin(UserAdmin):

    # Register your models here.
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active','role')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

    # Настройки редактирования пользователя (удаляем username)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name','role')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )

    # Настройки добавления пользователя (убираем username)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'is_staff', 'is_active', 'role'),
        }),
    )

admin.site.register(Employee, EmployeeAdmin)
