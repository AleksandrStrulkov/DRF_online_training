from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from online_training.models import Payments, Course
from users.models import User


class PaymentsSerializer(serializers.ModelSerializer):
	user = SlugRelatedField(slug_field='email', queryset=User.objects.all())
	payment_course = SlugRelatedField(slug_field='title', queryset=Course.objects.all())

	class Meta:
		model = Payments
		fields = '__all__'