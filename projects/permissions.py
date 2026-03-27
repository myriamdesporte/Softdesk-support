from rest_framework.permissions import BasePermission, SAFE_METHODS

from .models import Contributor


class IsAuthor(BasePermission):
    """
    Permission to allow only authors to edit their objects.
    Authenticated users can read.
    """

    def has_object_permission(self, request, view, obj):
        """
        Read permissions are allowed to any authenticated user.
        Write permissions are only allowed to the author.
        """
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


class IsProjectContributor(BasePermission):
    """
    Permission to check if user is a contributor of the project.
    """

    def has_permission(self, request, view):
        """Check if user is contributor of the project."""
        project_id = view.kwargs.get('project_pk')
        if not project_id:
            return True

        return Contributor.objects.filter(
            project_id=project_id,
            user=request.user
        ).exists()
