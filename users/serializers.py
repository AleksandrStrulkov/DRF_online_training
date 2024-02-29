from rest_framework import serializers

from online_training.serializers.payments import PaymentsSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"




