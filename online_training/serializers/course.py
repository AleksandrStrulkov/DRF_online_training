from rest_framework import serializers
from online_training.models import Course, Subscription
from online_training.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lesson = LessonSerializer(read_only=True, many=True)
    subscription = serializers.SerializerMethodField()
    # owner = SlugRelatedField(slug_field='email', queryset=User.objects.all())
    # owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def get_lessons_count(self, obj):
        if obj.lesson.all():
            return obj.lesson.all().count()
        return 0

    def get_subscription(self, obj):
        return Subscription.objects.filter(course=obj,
                                           user=self.context['request'].
                                           user).exists()

    class Meta:
        model = Course
        fields = '__all__'
