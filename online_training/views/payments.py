from rest_framework.generics import ListAPIView
from online_training.models import Payments
from online_training.serializers.payments import PaymentsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter


class APIPayments(ListAPIView):
	queryset = Payments.objects.all()
	serializer_class = PaymentsSerializer
	filter_backends = [DjangoFilterBackend, OrderingFilter]
	filterset_fields = ('payment_course', 'payment_method',)
	ordering_fields = ('date_payment',)
