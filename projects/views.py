from rest_framework.viewsets import ModelViewSet

from projects.models import Project, Contributor
from projects.serializers import ProjectSerializer, ContributorSerializer


class ProjectViewSet(ModelViewSet):
    """ViewSet for Project model."""
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()

    def perform_create(self, serializer):
        """
        Set the author to the current user when creating a project.
        Automatically add the author as a contributor.
        """
        project = serializer.save(author=self.request.user)
        Contributor.objects.create(user=self.request.user, project=project)


class ContributorViewSet(ModelViewSet):
    """
    ViewSet for Contributor model.
    """
    serializer_class = ContributorSerializer

    def get_queryset(self):
        return Contributor.objects.all()