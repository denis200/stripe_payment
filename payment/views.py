from locale import currency
from django.shortcuts import render
import stripe
import environ
from rest_framework import views,response
from goods.models import Item, Order

env = environ.Env(DEBUG=(bool, False))
stripe.api_key = env('SKSTRIPE')

class GetSessionView(views.APIView):
    """ PS. Очень интересно как происходит конвертация валют.В доке не нашел."""
    def get(self,request,pk):
        order = Order.objects.get(pk=pk)
        items = order.items.all()
        currency = items[0].currency
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': currency,
                    'product_data': {
                    'name': item.name
                    },
                    'unit_amount': int(str(item.price).replace('.','')),
                },
            'quantity': 1,
            } for item in items],
            mode='payment',
            success_url='http://127.0.0.1:8000/success',
            cancel_url='http://127.0.0.1:8000/cancel',
        )
        return response.Response({'session_id':session.id})


def success_view(request):
    return render(request,'success.html')


def cancel_view(request):
    return render(request,'cancel.html')

