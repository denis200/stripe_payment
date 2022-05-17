from django.urls import path
from goods.views import ItemDetailView, ItemListView, MakeOrderView


urlpatterns = [
    path('item/<int:pk>/', ItemDetailView.as_view(),name ='item'),
    path('',ItemListView.as_view()),
    path('makeorder/',MakeOrderView.as_view())

]
