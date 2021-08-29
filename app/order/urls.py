from django.urls import path
from .views import CreateOrderApiView


# api/orders/
urlpatterns = [
    path("create/", CreateOrderApiView.as_view(), name="order-create"),
]
