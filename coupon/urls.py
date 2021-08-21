from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

from .views import CouponRetriveViewByCode, CouponModelViewSet

coupon_router = DefaultRouter()
coupon_router.register(
    "", CouponModelViewSet, basename="coupon"
)  # /api/coupon/


urlpatterns = [
    path(
        "course/<str:course_id>/code/<str:code>",
        CouponRetriveViewByCode.as_view(),
        name="coupon-by-code",
    ),
    path("", include(coupon_router.urls)),
]
