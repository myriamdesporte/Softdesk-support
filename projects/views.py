from rest_framework.viewsets import ModelViewSet

from projects.models import Project, Contributor
from projects.serializers import ProjectSerializer, ContributorSerializer


class ProjectViewSet(ModelViewSet):
    """ViewSet for Project model."""
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()


class ContributorViewSet(ModelViewSet):
    """
    ViewSet for Contributor model.
    """
    serializer_class = ContributorSerializer

    def get_queryset(self):
        return Contributor.objects.all()