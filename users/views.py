from rest_framework.viewsets import ModelViewSet
from users.models import User


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
