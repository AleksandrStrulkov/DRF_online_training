from rest_framework import serializers

from online_training.models import Course


class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = '__all__'