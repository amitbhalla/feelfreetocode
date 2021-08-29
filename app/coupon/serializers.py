from rest_framework.serializers import ModelSerializer

from coupon.models import Coupon


class CouponSerializer(ModelSerializer):
    class Meta:
        model = Coupon
        fields = "__all__"
