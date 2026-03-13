from rest_framework import serializers

from projects.models import Project, Contributor


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
        read_only_fields = ['id', 'created_time']
