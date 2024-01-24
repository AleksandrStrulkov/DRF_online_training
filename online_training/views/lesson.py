from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from online_training.models import Lesson
from online_training.serializers.lesson import LessonSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated


class APILesson(ListCreateAPIView):
	queryset = Lesson.objects.all()
	serializer_class = LessonSerializer
	filter_backends = [DjangoFilterBackend, OrderingFilter]
	filterset_fields = ('title', 'course',)
	permission_classes = [IsAuthenticated]


class APILessonDetail(RetrieveUpdateDestroyAPIView):
	queryset = Lesson.objects.all()
	serializer_class = LessonSerializer
	permission_classes = [IsAuthenticated]

