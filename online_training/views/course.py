from rest_framework.viewsets import ModelViewSet

from online_training.models import Course
from online_training.serializers.course import CourseSerializer
from rest_framework.permissions import IsAuthenticated


class CourseViewSet(ModelViewSet):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		new_course = serializer.save()
		new_course.owner = self.request.user
		new_course.save()


