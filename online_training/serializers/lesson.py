from rest_framework import serializers

from online_training.models import Lesson, Course
from rest_framework.relations import SlugRelatedField


class LessonSerializer(serializers.ModelSerializer):
	course = SlugRelatedField(slug_field='title', queryset=Course.objects.all())

	class Meta:
		model = Lesson
		fields = '__all__'