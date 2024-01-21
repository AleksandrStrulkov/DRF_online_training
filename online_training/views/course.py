from rest_framework.viewsets import ModelViewSet

from online_training.models import Course
from online_training.serializers.course import CourseSerializer


class CourseViewSet(ModelViewSet):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer
