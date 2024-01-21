from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from online_training.models import Lesson
from online_training.serializers.lesson import LessonSerializer


class APILesson(ListCreateAPIView):
	queryset = Lesson.objects.all()
	serializer_class = LessonSerializer


class APILessonDetail(RetrieveUpdateDestroyAPIView):
	queryset = Lesson.objects.all()
	serializer_class = LessonSerializer