from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from online_training.models import Lesson
from online_training.paginators import VehiclePagination
from online_training.permissions import IsOwnerOrStaff
from online_training.serializers.lesson import LessonSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.exceptions import PermissionDenied


class APILesson(ListCreateAPIView):
	queryset = Lesson.objects.all()
	serializer_class = LessonSerializer
	filter_backends = [DjangoFilterBackend, OrderingFilter]
	filterset_fields = ('title', 'course',)
	permission_classes = [IsAuthenticated]
	pagination_class = VehiclePagination

	def perform_create(self, serializer):
		new_lesson = serializer.save()
		new_lesson.owner = self.request.user
		new_lesson.save()

	def post(self, request, *args, **kwargs):
		if not request.user.groups.filter(name='moderator'):
			return self.create(request, *args, **kwargs)
		raise PermissionDenied

	def get_queryset(self):
		if self.request.user.groups.filter(name='moderator') or self.request.user.is_staff:
			return Lesson.objects.all()
		elif not self.request.user.groups.filter(name='moderator'):
			return Lesson.objects.filter(owner=self.request.user)
		else:
			raise PermissionDenied


class APILessonDetail(RetrieveUpdateDestroyAPIView):
	queryset = Lesson.objects.all()
	serializer_class = LessonSerializer
	permission_classes = [IsAuthenticated]

	def delete(self, request, *args, **kwargs):
		if not request.user.groups.filter(name='moderator'):
			return self.destroy(request, *args, **kwargs)
		raise PermissionDenied

	def get_queryset(self):
		if self.request.user.groups.filter(name='moderator') or self.request.user.is_staff:
			return Lesson.objects.all()
		elif not self.request.user.groups.filter(name='moderator'):
			return Lesson.objects.filter(owner=self.request.user)
		else:
			raise PermissionDenied
