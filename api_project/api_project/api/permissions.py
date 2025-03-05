from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only admins to edit, but everyone can read.
    """

    def has_permission(self, request, view):
        # Allow GET, HEAD, or OPTIONS requests (read-only)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed for admin users
        return request.user and request.user.is_staff
