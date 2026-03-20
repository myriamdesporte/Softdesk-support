from rest_framework import routers
from rest_framework_nested import routers as nested_routers
from django.urls import path, include

from projects.views import ProjectViewSet, ContributorViewSet

router = routers.SimpleRouter()
router.register('projects', ProjectViewSet, basename='project')

projects_router = nested_routers.NestedSimpleRouter(router, 'projects', lookup='project')
projects_router.register('contributors', ContributorViewSet, basename='project-contributors')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(projects_router.urls)),
]
