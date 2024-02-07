from DRF_online_training import settings
from online_training.models import Subscription, Course
from django.core.mail import send_mail
from celery import shared_task


@shared_task
def message_update_course(course_id):
	users = [sub.user for sub in Subscription.objects.filter(course=course_id, is_active=True)]
	course = Course.objects.get(pk=course_id)
	send_mail(
			subject=f'Обновление курса {course.title}',
			message=f'Курс {course.title} был обновлён',
			from_email=settings.DEFAULT_FROM_EMAIL,
			recipient_list=[user.email for user in users]
	)
	print("Отправлено")



