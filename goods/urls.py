from django.urls import path
from goods.views import ItemDetailView, cancel_view, item_view, success_view


urlpatterns = [
    path('item/<int:pk>',item_view),
    path('detail/<int:pk>/', ItemDetailView.as_view(), name = 'detail'),
    path('success/',success_view()),
    path('cansel/',cancel_view()),

]
