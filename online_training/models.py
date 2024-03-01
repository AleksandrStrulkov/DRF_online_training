from django.db import models
from django.db import connection
from django.contrib.auth import get_user_model

NULLABLE = {'blank': True, 'null': True}

PAY_METHOD = (
    ('Наличные', 'Наличные'),
    ('Перевод', 'Перевод')
)


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название курса')
    preview = models.ImageField(upload_to='images_course/',
                                verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание')
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                              **NULLABLE)
    price = models.DecimalField(default=100, max_digits=8, decimal_places=2,
                                verbose_name='Цена курса')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    @classmethod
    def truncate_table_restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'ALTER SEQUENCE '
                           f'catalog_statusproduct_id_seq RESTART WITH 1;')


class Lesson(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='images_lesson/',
                                verbose_name='Превью', **NULLABLE)
    video = models.URLField(verbose_name='Ссылка на видео', **NULLABLE)
    course = models.ForeignKey(
        Course, verbose_name='Курс', on_delete=models.CASCADE, **NULLABLE,
        related_name="lesson"
    )
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                              **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

    @classmethod
    def truncate_table_restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'ALTER SEQUENCE '
                           f'catalog_statusproduct_id_seq RESTART WITH 1;')


class Payments(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL,
        verbose_name='Пользователь', **NULLABLE,
        related_name="payments"
    )
    date_payment = models.DateField(verbose_name='Дата оплаты',
                                    auto_now_add=True)
    payment_course = models.ForeignKey(
        Course, verbose_name='Оплаченный курс', on_delete=models.CASCADE,
        **NULLABLE,
        related_name="payments"
    )
    payment_amount = models.IntegerField(verbose_name='Сумма оплаты',
                                         **NULLABLE)
    payment_method = models.CharField(choices=PAY_METHOD, default='Cash',
                                      max_length=10,
                                      verbose_name='Способ оплаты')
    is_paid = models.BooleanField(default=False, verbose_name='Статус платежа')
    session_id = models.CharField(max_length=200,
                                  verbose_name='Сессия для оплаты', **NULLABLE)

    def __str__(self):
        return f'{self.user} - {self.date_payment}'

    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'оплаты'

    @classmethod
    def truncate_table_restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'ALTER SEQUENCE '
                           f'catalog_statusproduct_id_seq RESTART WITH 1;')


class Subscription(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                             verbose_name='Пользователь', **NULLABLE)
    course = models.ForeignKey(Course, related_name='subscription',
                               on_delete=models.CASCADE, **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='Подписка',
                                    **NULLABLE)

    def __str__(self):
        return f'{self.user} - {self.course}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
