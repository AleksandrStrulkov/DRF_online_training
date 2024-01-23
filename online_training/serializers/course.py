from rest_framework import serializers

from online_training.models import Course, Lesson
from online_training.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
	lessons_count = serializers.SerializerMethodField()

	def get_lessons_count(self, obj):
		if obj.lesson.all():
			return obj.lesson.all().count()
		return 0

	class Meta:
		model = Course
		fields = '__all__'