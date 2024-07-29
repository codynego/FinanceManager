from rest_framework import permissions

class AdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if (request.user.is_staff or request.user.is_super_user) and request.user.is_authenticated:
            return True
        return False