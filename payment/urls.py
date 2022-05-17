from django.urls import path
from payment.views import GetSessionView, cancel_view,success_view


urlpatterns = [
    path('buy/<int:pk>',GetSessionView.as_view()),
    path('success/',success_view),
    path('canсel/',cancel_view)

]
