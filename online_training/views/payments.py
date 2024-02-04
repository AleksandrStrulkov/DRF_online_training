from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, get_object_or_404
from online_training.models import Payments
from online_training.serializers.payments import PaymentsSerializer, PaymentsCreateSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers

from online_training.services import get_session, retrieve_session


class APIPayments(ListAPIView):
	queryset = Payments.objects.all()
	serializer_class = PaymentsSerializer
	filter_backends = [DjangoFilterBackend, OrderingFilter]
	filterset_fields = ('payment_course', 'payment_method',)
	ordering_fields = ('date_payment',)
	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		if not self.request.user.is_staff:
			return Payments.objects.filter(user=self.request.user)
		return Payments.objects.all()


class PaymentCreateAPIView(CreateAPIView):
	serializer_class = PaymentsCreateSerializer

	def perform_create(self, serializer):
		course = serializer.validated_data.get('payment_course')
		payment = serializer.save()
		payment.user = self.request.user
		if payment.payment_method == 'Перевод':
			payment.session_id = get_session(payment).id
			payment.payment_amount = payment.payment_course.price
		payment.save()


class PaymentRetrieveAPIView(RetrieveAPIView):
	serializer_class = PaymentsSerializer
	queryset = Payments.objects.all()

	def get_object(self):
		obj = get_object_or_404(self.get_queryset(), pk=self.kwargs['pk'])
		if obj.session_id:
			session_id = retrieve_session(obj.session_id)
			if session_id.payment_status == 'paid' and session_id.status == 'complete':
				obj.is_paid = True
				obj.save()

		self.check_object_permissions(self.request, obj)
		return obj
