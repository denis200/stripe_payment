from django.views.generic import DetailView,ListView
from rest_framework.views import APIView
from rest_framework.response import Response
from goods.models import Item, Order
from django.db.models import Sum


class ItemListView(ListView):
    model = Item
    template_name = 'items.html'


class ItemDetailView(DetailView):
    queryset = Item.objects.all()
    template_name = 'item.html'


class MakeOrderView(APIView):
    """ При запросе принимается список товаров и создается модель Order"""
    def post(self,request):
        items = Item.objects.filter(pk__in = request.data)
        total_price = items.aggregate(Sum('price'))
        order = Order.objects.create(total_price = total_price['price__sum'])
        order.save()
        for item in items:
            order.items.add(item.pk)
        return Response({'order_id':order.id})