from rest_framework.generics import ListCreateAPIView

from online_training.models import Payments
from online_training.serializers.payments import PaymentsSerializer


class APIPayments(ListCreateAPIView):
	queryset = Payments.objects.all()
	serializer_class = PaymentsSerializer
