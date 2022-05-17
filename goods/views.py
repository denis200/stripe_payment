from django.views.generic import DetailView,ListView

from goods.models import Item


class ItemListView(ListView):
    model = Item
    template_name = 'items.html'


class ItemDetailView(DetailView):
    queryset = Item.objects.all()
    template_name = 'item.html'