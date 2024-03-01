from rest_framework import serializers
from online_training.models import Lesson, Course
from rest_framework.relations import SlugRelatedField
from online_training.validators import LessonVideoValidator


class LessonSerializer(serializers.ModelSerializer):
    course = SlugRelatedField(slug_field='title',
                              queryset=Course.objects.all())
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LessonVideoValidator(field='video')]
