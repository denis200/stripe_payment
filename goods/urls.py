from django.urls import path
from goods.views import ItemDetailView, ItemListView


urlpatterns = [
    path('item/<int:pk>/', ItemDetailView.as_view(),name ='item'),
    path('items/',ItemListView.as_view())

]
