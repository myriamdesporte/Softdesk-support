from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import User
from .permissions import IsOwner
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """
    ViewSet for User model.
    Allows CRUD operations on users.
    """

    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    def get_permissions(self):
        """
        Allow anyone to create an account.
        Other actions require authentication.
        """
        if self.action == 'create':
            return [AllowAny()]
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsOwner()]
        return [IsAuthenticated()]
