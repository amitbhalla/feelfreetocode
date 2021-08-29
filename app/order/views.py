from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    OrderSerializer,
    OrderItemSerializer,
    SubscriptionSerializer,
)


class CreateOrderApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            return Response("ok")
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
