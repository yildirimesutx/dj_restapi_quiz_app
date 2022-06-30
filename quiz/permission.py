from rest_framework import permissions

class IsAuthOrNot(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return bool(request.user.is_authenticated or request.user.is_staff)
        else :
            return False