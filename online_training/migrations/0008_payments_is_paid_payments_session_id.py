# Generated by Django 5.0.1 on 2024-02-04 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_training', '0007_alter_course_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='Статус платежа'),
        ),
        migrations.AddField(
            model_name='payments',
            name='session_id',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Сессия для оплаты'),
        ),
    ]