from rest_framework import serializers

from projects.models import Project, Contributor, Issue, Comment


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for Project model."""

    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'description',
            'type',
            'author',
            'created_time'
        ]
        read_only_fields = ['id', 'author', 'created_time']


class ContributorSerializer(serializers.ModelSerializer):
    """Serializer for Contributor model."""
    username = serializers.ReadOnlyField(source='user.username')
    project_name = serializers.ReadOnlyField(source='project.name')

    class Meta:
        model = Contributor
        fields = [
            'id',
            'user',
            'username',
            'project',
            'project_name',
            'created_time',
        ]
        read_only_fields = ['id', 'project', 'created_time']


class IssueSerializer(serializers.ModelSerializer):
    """Serializer for Issue model."""
    author = serializers.ReadOnlyField(source='author.username')
    assignee_username = serializers.ReadOnlyField(source='assignee.username')
    project_name = serializers.ReadOnlyField(source='project.name')

    class Meta:
        model = Issue
        fields = [
            'id', 'title', 'description', 'priority', 'tag', 'status',
            'project', 'project_name', 'author', 'assignee', 'assignee_username',
            'created_time'
        ]
        read_only_fields = ['id', 'author', 'project', 'created_time']

    def validate_assignee(self, value):
        """Validate that assignee is a contributor of the project."""
        if value:
            project = self.initial_data.get('project') if self.initial_data else None
            if not project and self.instance:
                project = self.instance.project.id

            if project and not Contributor.objects.filter(project_id=project, user=value).exists():
                raise serializers.ValidationError(
                    "Assignee must be a contributor of this project."
                )

        return value


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment model."""
    author = serializers.ReadOnlyField(source='author.username')
    issue_title = serializers.ReadOnlyField(source='issue.title')

    class Meta:
        model = Comment
        fields = ['id', 'uuid', 'description', 'author', 'issue', 'issue_title', 'created_time']
        read_only_fields = ['id', 'uuid', 'author', 'issue', 'created_time']
