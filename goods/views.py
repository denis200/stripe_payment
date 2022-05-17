from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, DeleteView
from rest_framework import views,response
import stripe
import environ

env = environ.Env(DEBUG=(bool, False))

from goods.models import Item

class GetSessionView(views.APIView):
    def get(self,request,pk):
        item = Item.objects.get(pk=pk)
        stripe.api_key = env('SKSTRIPE')
        session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'rub',
                'product_data': {
                'name': item.name,
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


class ItemDetailView(DetailView):
    queryset = Item.objects.all()
    template_name = 'item.html'