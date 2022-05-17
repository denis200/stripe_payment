from django.urls import path
from goods.views import GetSessionView, ItemDetailView, cancel_view,success_view


urlpatterns = [
    path('buy/<int:pk>',GetSessionView.as_view()),
    path('item/<int:pk>/', ItemDetailView.as_view()),
    path('success/',success_view),
    path('canсel/',cancel_view)

]
