from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import JSONParser

from course.serializers import CategorySerializer
from course.models import Category


@api_view(['GET'])
def test_view(request):
    response = {
        'message': 'Course API is working',
        'url': request.get_full_path(),
    }
    return Response(response)


class CategoryListView(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        json = JSONParser().parse(request)
        serializer = CategorySerializer(data=json)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)
