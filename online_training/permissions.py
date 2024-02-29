from rest_framework.permissions import BasePermission
from rest_framework import permissions


class IsOwnerOrStaff(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user or request.user.is_staff