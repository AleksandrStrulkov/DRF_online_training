from django.urls import path
from rest_framework import routers

from online_training.apps import OnlineTrainingConfig
from online_training.views.course import CourseViewSet
from online_training.views.lesson import LessonCreateView, LessonListView, LessonDetailView, LessonUpdateView, \
	LessonDeleteView

app_name = OnlineTrainingConfig.name

urlpatterns = [
	path('api/lesson/create/', LessonCreateView.as_view(), name='lesson-create'),
	path('api/lesson/', LessonListView.as_view(), name='lesson-list'),
	path('api/lesson/<int:pk>/', LessonDetailView.as_view(), name='lesson-get'),
	path('api/lesson/update/<int:pk>/', LessonUpdateView.as_view(), name='lesson-update'),
	path('api/lesson/delete/<int:pk>/', LessonDeleteView.as_view(), name='lesson-delete'),

]

router = routers.SimpleRouter()
router.register(r'api/course', CourseViewSet, basename='курс')

urlpatterns += router.urls
