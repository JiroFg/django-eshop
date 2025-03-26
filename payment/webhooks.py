import json
import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order
from .tasks import payment_completed
from shop.models import Product
from shop.recommender import Recommender

stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    event = None
    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        return HttpResponse(status=400)
    if event.type == 'checkout.session.completed':
        session = event.data.object
        if(session.mode == 'payment' and session.payment_status == 'paid'):
            try:
                order = Order.objects.get(
                    id=session.client_reference_id
                )
                order.paid = True
                order.stripe_id = session.payment_intent
                order.save()
                product_ids = order.items.values_list('product_id')
                products = Product.objects.filter(id__in=product_ids)
                r = Recommender()
                r.products_bought(products)
                payment_completed.delay(order.id)
            except Order.DoesNotExist:
                return HttpResponse(status=404)
    return HttpResponse(status=200)