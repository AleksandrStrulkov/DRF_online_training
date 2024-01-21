from rest_framework.generics import RetrieveAPIView, DestroyAPIView, ListAPIView, UpdateAPIView, CreateAPIView

from online_training.models import Lesson
from online_training.serializers.lesson import LessonSerializer


class LessonDetailView(RetrieveAPIView):
	queryset = Lesson.objects.all()
	serializer_class = LessonSerializer


class LessonListView(ListAPIView):
	queryset = Lesson.objects.all()
	serializer_class = LessonSerializer


class LessonCreateView(CreateAPIView):
	queryset = Lesson.objects.all()
	serializer_class = LessonSerializer


class LessonUpdateView(UpdateAPIView):
	queryset = Lesson.objects.all()
	serializer_class = LessonSerializer


class LessonDeleteView(DestroyAPIView):
	queryset = Lesson.objects.all()
	serializer_class = LessonSerializer

