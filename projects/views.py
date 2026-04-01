from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Project, Contributor, Issue, Comment
from .serializers import (
    ProjectSerializer,
    ContributorSerializer,
    IssueSerializer,
    CommentSerializer,
)
from .permissions import IsAuthor, IsProjectContributor


class ProjectViewSet(ModelViewSet):
    """ViewSet for Project model."""

    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

    def get_queryset(self):
        """Return only projects where user is a contributor or author."""
        return Project.objects.filter(contributors__user=self.request.user).distinct()

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
    permission_classes = [IsAuthenticated, IsProjectContributor]

    def get_queryset(self):
        """Filter contributors by project."""
        project_id = self.kwargs.get("project_pk")
        if project_id:
            return Contributor.objects.filter(project_id=project_id)
        return Contributor.objects.none()

    def perform_create(self, serializer):
        """Automatically set the project from URL."""
        project_id = self.kwargs.get("project_pk")
        if project_id:
            serializer.save(project_id=project_id)


class IssueViewSet(ModelViewSet):
    """ViewSet for Issue model."""

    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IsProjectContributor, IsAuthor]

    def get_queryset(self):
        """Filter issues by project."""
        project_id = self.kwargs.get("project_pk")
        if project_id:
            return Issue.objects.filter(project_id=project_id)
        return Issue.objects.none()

    def perform_create(self, serializer):
        """Set the author and project when creating an issue."""
        project_id = self.kwargs.get("project_pk")
        if project_id:
            serializer.save(author=self.request.user, project_id=project_id)


class CommentViewSet(ModelViewSet):
    """ViewSet for Comment model."""

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsProjectContributor, IsAuthor]

    def get_queryset(self):
        """Filter comments by issue."""
        issue_id = self.kwargs.get("issue_pk")
        if issue_id:
            return Comment.objects.filter(issue_id=issue_id)
        return Comment.objects.none()

    def perform_create(self, serializer):
        """Set the author and issue when creating a comment."""
        issue_id = self.kwargs.get("issue_pk")
        if issue_id:
            serializer.save(author=self.request.user, issue_id=issue_id)
