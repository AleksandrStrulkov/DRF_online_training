from rest_framework import serializers

from online_training.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Lesson
		fields = '__all__'