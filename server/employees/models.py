from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager

class EmployeeManager(BaseUserManager):
    """
    Кастомный менеджер для модели Employee, где email используется вместо username.
    """

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        groups = extra_fields.pop('groups', None)
        user_permissions = extra_fields.pop('user_permissions', None)

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        if groups:
            user.groups.set(groups)  # Use `.set()` for many-to-many fields

        if user_permissions:
            user.user_permissions.set(user_permissions)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Создание суперпользователя.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class Employee(AbstractUser):
    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    class Roles(models.TextChoices):
        SELECT = "Select", "Select"
        BACK_DEV = "Backend Dev", "Backend Dev"
        FRONT_DEV = "Frontend Dev", "Frontend Dev"
        TESTER = "tester", "tester"
        DISIGNER = "Designer", "Designer"

    username = None

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = EmployeeManager()

    email = models.EmailField(_("email address"), blank=True, unique=True)
    role = models.CharField(max_length=20, choices=Roles, default=Roles.SELECT)

    def __str__(self):
        return self.get_full_name()


