from django.urls import path
from rest_framework import routers

from online_training.apps import OnlineTrainingConfig
from online_training.views.course import CourseViewSet
from online_training.views.lesson import APILessonDetail, APILesson
from online_training.views.payments import APIPayments, PaymentCreateAPIView, PaymentRetrieveAPIView
from online_training.views.subscription import SubscriptionCreateAPIView, SubscriptionDestroyAPIView

app_name = OnlineTrainingConfig.name

urlpatterns = [
    path('api/lesson/', APILesson.as_view()),
    path('api/lesson/<int:pk>/', APILessonDetail.as_view()),

    path('api/payments/', APIPayments.as_view()),
    path('api/payments/create/', PaymentCreateAPIView.as_view()),
    path('api/payments/<int:pk>/', PaymentRetrieveAPIView.as_view()),

    path('subscription/', SubscriptionCreateAPIView.as_view()),
    path('subscription/delete/<int:pk>/', SubscriptionDestroyAPIView.as_view()),
]

router = routers.SimpleRouter()
router.register(r'api/course', CourseViewSet, basename='курс')

urlpatterns += router.urls