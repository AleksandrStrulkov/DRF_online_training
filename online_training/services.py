import stripe

from django.conf import settings
from online_training.models import Payments
from decimal import *

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


def get_session(serializer: Payments):
	course_title = serializer.payment_course.title
	product = stripe.Product.create(name=course_title)

	price_data = {
		'unit_amount': int(serializer.payment_course.price * Decimal('100')),
		'currency': 'rub',
		'product': product.id,
		}

	price = stripe.Price.create(**price_data)

	session_data = {
		'success_url': 'https://example.com/success',
		'line_items': [{'price': price.id, 'quantity': 1}],
		'mode': 'payment',
		'customer_email': serializer.user.email,
	}

	session = stripe.checkout.Session.create(**session_data)

	print(session.url)

	return session


def retrieve_session(session):
	return stripe.checkout.Session.retrieve(session)
