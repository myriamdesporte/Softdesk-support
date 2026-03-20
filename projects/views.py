from rest_framework.viewsets import ModelViewSet

from projects.models import Project, Contributor, Issue, Comment
from projects.serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer


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


class IssueViewSet(ModelViewSet):
    """ViewSet for Issue model."""
    serializer_class = IssueSerializer

    def get_queryset(self):
        """Return only issues belonging to the project in the URL."""
        project_id = self.kwargs.get('project_pk')
        if project_id:
            return Issue.objects.filter(project_id=project_id)
        return Issue.objects.all()

    def perform_create(self, serializer):
        """Set the author and project when creating an issue."""
        project_id = self.kwargs.get('project_pk')
        if project_id:
            serializer.save(author=self.request.user, project_id=project_id)
        else:
            serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    """ViewSet for Comment model."""
    serializer_class = CommentSerializer

    def get_queryset(self):
        """Return only comments belonging to the issue in the URL"""
        issue_id = self.kwargs.get('issue_pk')
        if issue_id:
            return Comment.objects.filter(issue_id=issue_id)
        return Comment.objects.all()

    def perform_create(self, serializer):
        """Set the author and issue when creating a comment."""
        issue_id = self.kwargs.get('issue_pk')
        if issue_id:
            serializer.save(author=self.request.user, issue_id=issue_id)
        else:
            serializer.save(author=self.request.user)