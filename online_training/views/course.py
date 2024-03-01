from rest_framework.viewsets import ModelViewSet
from online_training.models import Course
from online_training.paginators import OnlineTrainingPagination
from online_training.serializers.course import CourseSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from online_training.tasks import message_update_course_task


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = OnlineTrainingPagination

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.groups.\
                filter(name='moderator'):
            return Course.objects.all()
        elif not self.request.user.is_staff:
            return Course.objects.filter(owner=self.request.user)
        else:
            raise PermissionDenied

    def perform_update(self, serializer):
        course_id = serializer.save(owner=self.request.user).id
        message_update_course_task.delay(course_id)
