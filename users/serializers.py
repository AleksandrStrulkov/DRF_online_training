from rest_framework import serializers

from online_training.serializers.payments import PaymentsSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
	payments = PaymentsSerializer(many=True, read_only=True)

	class Meta:
		model = User
		# fields = ("id", "first_name", "email", "payments",)
		fields = "__all__"


class UserOwnerSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ("id", "first_name", "email", )

