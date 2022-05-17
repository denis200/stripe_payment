from django.shortcuts import render
import stripe
import environ
from rest_framework import views,response
from goods.models import Item

env = environ.Env(DEBUG=(bool, False))


class GetSessionView(views.APIView):
    def get(self,request,pk):
        item = Item.objects.get(pk=pk)
        stripe.api_key = env('SKSTRIPE')
        session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'rub',
                'product_data': {
                'name': item.name
                },
                'unit_amount': int(str(item.price).replace('.','')),
            },
            'quantity': 1,
            }],
            mode='payment',
            success_url='http://127.0.0.1:8000/success',
            cancel_url='http://127.0.0.1:8000/cancel',
        )
        return response.Response({'session_id':session.id})


def success_view(request):
    return render(request,'success.html')


def cancel_view(request):
    return render(request,'cancel.html')

