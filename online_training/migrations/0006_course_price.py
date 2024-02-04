# Generated by Django 5.0.1 on 2024-02-03 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_training', '0005_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.DecimalField(decimal_places=2, default=100000, max_digits=8, verbose_name='Цена курса'),
        ),
    ]
