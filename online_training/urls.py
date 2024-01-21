from django.urls import path
from rest_framework import routers

from online_training.apps import OnlineTrainingConfig
from online_training.views.course import CourseViewSet
from online_training.views.lesson import APILessonDetail, APILesson

app_name = OnlineTrainingConfig.name

urlpatterns = [
	path('api/lesson/', APILesson.as_view()),
	path('api/lesson/<int:pk>/', APILessonDetail.as_view()),
]

router = routers.SimpleRouter()
router.register(r'api/course', CourseViewSet, basename='курс')

urlpatterns += router.urls
