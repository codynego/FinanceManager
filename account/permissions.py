from rest_framework import permissions

class GetAccountPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            if request.user.is_staff and request.user.is_authenticated:
                return True
        elif request.method == "POST":
            if request.user.is_authenticated:
                return True
            
        return False