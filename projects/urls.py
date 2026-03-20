from rest_framework import routers
from rest_framework_nested import routers as nested_routers
from django.urls import path, include

from projects.views import ProjectViewSet, ContributorViewSet, IssueViewSet, CommentViewSet

router = routers.SimpleRouter()
router.register('projects', ProjectViewSet, basename='project')

projects_router = nested_routers.NestedSimpleRouter(router, 'projects', lookup='project')
projects_router.register('contributors', ContributorViewSet, basename='project-contributors')
projects_router.register('issues', IssueViewSet, basename='project-issues')

issues_router = nested_routers.NestedSimpleRouter(projects_router, 'issues', lookup='issue')
issues_router.register('comments', CommentViewSet, basename='issue_comments')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(projects_router.urls)),
    path('', include(issues_router.urls))
]
