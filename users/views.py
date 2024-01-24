from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated


class UsersViewSet(ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [IsAuthenticated]


