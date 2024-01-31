from online_training.models import Subscription
from online_training.serializers.subscription import SubscriptionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class SubscriptionCreateAPIView(ListCreateAPIView):
	serializer_class = SubscriptionSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

	def get_queryset(self):
		return Subscription.objects.filter(user=self.request.user)


class SubscriptionDestroyAPIView(RetrieveUpdateDestroyAPIView):
	serializer_class = SubscriptionSerializer
	queryset = Subscription.objects.all()
	permission_classes = [IsAuthenticated]
