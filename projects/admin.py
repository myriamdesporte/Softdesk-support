from django.contrib import admin
from .models import Project, Contributor


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Admin for Project model."""
    list_display = ('name', 'type', 'description', 'author', 'created_time')
    list_filter = ('type', 'created_time')
    search_fields = ('name', 'description')
    readonly_fields = ('created_time',)

    def save_model(self, request, obj, form, change):
        """
        Automatically add the author as a contributor when creating a project.
        """
        super().save_model(request, obj, form, change)

        if not change:
            Contributor.objects.get_or_create(user=obj.author, project=obj)


@admin.register(Contributor)
class ContributorAdmin(admin.ModelAdmin):
    """Admin for Contributor model."""
    list_display = ('user', 'project', 'created_time')
    list_filter = ('created_time',)
    search_fields = ('user__username', 'project__name')
    readonly_fields = ('created_time',)