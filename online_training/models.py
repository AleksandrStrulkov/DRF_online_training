from django.conf import settings
from django.db import models
from django.db import connection
from django.contrib.auth import get_user_model

NULLABLE = {'blank': True, 'null': True}

PAY_METHOD = (
		(None, 'Выберите способ оплаты'),
		('Cash', 'Наличные'),
		('Transfer', 'Перевод')
)


class Course(models.Model):
	title = models.CharField(max_length=150, verbose_name='Название курса')
	preview = models.ImageField(upload_to='images_course/', verbose_name='Превью', **NULLABLE)
	description = models.TextField(verbose_name='Описание')
	owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, **NULLABLE)

	def __str__(self):
		return f'{self.title}'

	class Meta:
		verbose_name = 'курс'
		verbose_name_plural = 'курсы'

	@classmethod
	def truncate_table_restart_id(cls):
		with connection.cursor() as cursor:
			cursor.execute(f'ALTER SEQUENCE catalog_statusproduct_id_seq RESTART WITH 1;')


class Lesson(models.Model):
	title = models.CharField(max_length=200, verbose_name='Название урока')
	description = models.TextField(verbose_name='Описание')
	preview = models.ImageField(upload_to='images_lesson/', verbose_name='Превью', **NULLABLE)
	video = models.URLField(verbose_name='Ссылка на видео', **NULLABLE)
	course = models.ForeignKey(
			Course, verbose_name='Курс', on_delete=models.CASCADE, **NULLABLE,
			related_name="lesson"
	)
	owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, **NULLABLE)

	def __str__(self):
		return f'{self.title}'

	class Meta:
		verbose_name = 'урок'
		verbose_name_plural = 'уроки'

	@classmethod
	def truncate_table_restart_id(cls):
		with connection.cursor() as cursor:
			cursor.execute(f'ALTER SEQUENCE catalog_statusproduct_id_seq RESTART WITH 1;')


class Payments(models.Model):
	user = models.ForeignKey(
		get_user_model(), on_delete=models.SET_NULL, verbose_name='Пользователь', **NULLABLE,
		related_name="payments"
		)
	date_payment = models.DateField(verbose_name='Дата оплаты')
	payment_course = models.ForeignKey(
		Course, verbose_name='Оплаченный курс', on_delete=models.CASCADE, **NULLABLE,
		related_name="payments"
		)
	payment_amount = models.IntegerField(verbose_name='Сумма оплаты')
	payment_method = models.CharField(choices=PAY_METHOD, default='Cash', max_length=10, verbose_name='Способ оплаты')

	def __str__(self):
		return f'{self.user} - {self.date_payment}'

	class Meta:
		verbose_name = 'оплата'
		verbose_name_plural = 'оплаты'

	@classmethod
	def truncate_table_restart_id(cls):
		with connection.cursor() as cursor:
			cursor.execute(f'ALTER SEQUENCE catalog_statusproduct_id_seq RESTART WITH 1;')