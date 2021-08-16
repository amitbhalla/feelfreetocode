from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView

from course.serializers import CategorySerializer
from course.models import Category


@api_view(['GET'])
def test_view(request):
    response = {
        'message': 'Course API is working',
        'url': request.get_full_path(),
    }
    return Response(response)


class CategoryListView(ListCreateAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
