from rest_framework import serializers

from online_training.models import Course, Lesson
from online_training.serializers.lesson import LessonSerializer
from rest_framework.relations import SlugRelatedField

from users.models import User


class CourseSerializer(serializers.ModelSerializer):
	lessons_count = serializers.SerializerMethodField()
	lesson = LessonSerializer(read_only=True, many=True)
	owner = SlugRelatedField(slug_field='email', queryset=User.objects.all())

	def get_lessons_count(self, obj):
		if obj.lesson.all():
			return obj.lesson.all().count()
		return 0

	class Meta:
		model = Course
		fields = '__all__'