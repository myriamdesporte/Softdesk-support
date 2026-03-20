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
    """ViewSet for Contributor model."""
    serializer_class = ContributorSerializer

    def get_queryset(self):
        """Filter contributors by project."""
        project_id = self.kwargs.get('project_pk')
        if project_id:
            return Contributor.objects.filter(project_id=project_id)
        return Contributor.objects.all()

    def perform_create(self, serializer):
        """Automatically set the project from URL."""
        project_id = self.kwargs.get('project_pk')
        if project_id:
            serializer.save(project_id=project_id)
        else:
            serializer.save()