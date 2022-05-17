from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, DeleteView
import stripe

from goods.models import Item

def item_view(request,pk):
    session = stripe.checkout.Session.create(
    line_items=[{
      'price_data': {
        'currency': 'usd',
        'product_data': {
          'name': 'T-shirt',
        },
        'unit_amount': 2000,
      },
      'quantity': 1,
    }],
    mode='payment',
    success_url='https://127.0.0.1:8080/success',
    cancel_url='https://127.0.0.1:8080/cancel',
  )
    return redirect(session.url)


def success_view(request):
    render(request,'success.html')


def cancel_view(request):
    render(request,'cansel.html')


class ItemDetailView(DetailView):
    queryset = Item.objects.all()
    template_name = 'item.html'