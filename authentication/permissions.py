from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Allow users to manage only their own profile"""

    def has_object_permission(self, request, view, obj):
        return obj == request.user
