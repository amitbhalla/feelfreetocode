import uuid

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from coupon.models import Coupon
from coupon.serializers import CouponSerializer
from course.models import Course


class CouponRetriveViewByCode(ListAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

    def get(self, request, *args, **kwargs):
        code = self.kwargs.get("code")
        course_id = self.kwargs.get("course_id")
        try:
            uuid.UUID(course_id)
        except ValueError:
            return Response(
                {"course_id": ["course_id is not a valid UUID format!"]},
                status=status.HTTP_400_BAD_REQUEST,
            )  # Using response because Django doesn't have a native ValueError

        self.queryset = self.queryset.filter(
            course=Course.objects.get(id=course_id), code=code, active=True
        )
        if len(self.queryset) == 0:
            error_message = {
                "coupon_code": "Nothing found for that coupon code!"
            }
            print(error_message)
            return Response(error_message, status=status.HTTP_404_NOT_FOUND)
        return super().get(request, *args, **kwargs)


class CouponModelViewSet(ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = [IsAdminUser]
