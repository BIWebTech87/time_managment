from rest_framework import permissions

class IsAuthenticatedAndSuperuser(permissions.BasePermission):
    """
    Custom permission to allow only authenticated users who are also admins.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser