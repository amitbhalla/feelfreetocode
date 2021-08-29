from rest_framework.serializers import ModelSerializer, CharField, UUIDField

from .models import Order, OrderItem, Subscription
from core.serializers import UserSerializer
from coupon.serializers import CouponSerializer


class OrderSerializer(ModelSerializer):
    order_id = CharField(max_length=150, required=False)
    user = UserSerializer(read_only=True)
    coupon = CouponSerializer(read_only=True)

    class Meta:
        model = Order
        fields = "__all__"


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
