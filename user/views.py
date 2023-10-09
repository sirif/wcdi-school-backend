from rest_framework import mixins, viewsets
from rest_framework import permissions

from user.models import User
from user.serializers import UserSerializer


class UserViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """
    Список пользователей - доступен только для администраторов
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

