from rest_framework import routers
from django.urls import path, include

from authentication.views import UserViewSet

router = routers.SimpleRouter()
router.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
