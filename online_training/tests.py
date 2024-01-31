from rest_framework.test import APITestCase
from rest_framework import status

from online_training.models import Course, Lesson, Subscription
from online_training.serializers.lesson import LessonSerializer
from users.models import User


class LessonTestCase(APITestCase):

	def setUp(self):
		self.user = User.objects.create(email='test@yandex.ru', is_active=True)
		self.user.set_password('test_1247')
		self.user.save()
		self.client.force_authenticate(user=self.user)

		self.course = Course.objects.create(
		title='Test course',
		description='Test description',
		owner=self.user
		)

		self.lesson = Lesson.objects.create(
		title='Test lesson',
		description='Test description',
		course=self.course,
		owner=self.user,
		)

	def test_create_lesson_(self):
		"""Тестирование создания уроков"""
		data = {
		'title': 'test lesson',
		'description': 'test description',
		'video': 'https://www.youtube.com/watch?v=bITQ13XCU9Q&list=PLA0M1Bcd0w8xZA3Kl1fYmOH_MfLpiYMRs&index=15',
		'course': self.course
		}
		response = self.client.post('/api/lesson/', data=data)
		print(response.json())
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_get_lesson(self):
		""" Тестирование вывода одного урока """

		response = self.client.get(f'/api/lesson/{self.lesson.pk}/')
		serializer_data = LessonSerializer(self.lesson).data

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(serializer_data, response.data)

	def test_update(self):
		""" Тестирование изменения урока """

		url = f'/api/lesson/{self.lesson.id}/'
		response = self.client.patch(url, {'title': 'new title test',
		'description': 'new description test',
		'course': self.course,
		'video': 'https://www.youtube.com/watch?v=fTLOX6x-GQg&t=101s'
		}
		)
		self.lesson.refresh_from_db()

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(self.lesson.title, 'new title test')
		self.assertEqual(self.lesson.description, 'new description test')

	def test_delete(self):
		""" Тестирование удаления урока """

		response = self.client.delete(f'/api/lesson/{self.lesson.id}/')

		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class SubscriptionTestCase(APITestCase):

	def setUp(self):
		self.user = User.objects.create(email='test@ya.ru', is_active=True)
		self.user.set_password('test_2369')
		self.user.save()
		self.client.force_authenticate(user=self.user)

		self.course = Course.objects.create(
		title='Test course',
		description='Test description',
		owner=self.user
		)

		self.subscription = Subscription.objects.create(
		user=self.user,
		course=self.course,
		is_active=True
		)

	def test_create_subscription(self):
		""" Тестирование создания подписки на курс """

		data = {
		'user': self.user.id,
		'course': self.course.id,
		'is_active': True
		}
		response = self.client.post('/subscription/', data=data)
		print(response.json())
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertTrue(Subscription.objects.filter(course=self.course.id, user=self.user.id, is_active=True))
		self.assertEqual(response.json(), {
		'id': 2,
		'is_active': True,
		'user': self.user.id,
		'course': self.course.id
		}
		)

	def test_delete_subscription(self):
		""" Тестирование удаления подписки на курс"""

		response = self.client.delete(f'/subscription/delete/{self.subscription.id}/')

		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
		self.assertFalse(Subscription.objects.filter(user=self.user.id,
		course=self.course.id,
		is_active=True))



