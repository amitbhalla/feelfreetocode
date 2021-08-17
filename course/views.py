from django.core.exceptions import ValidationError

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status

from core.permissions import IsAdminUserOrReadOnly
from course.serializers import CategorySerializer, CourseSerializer, TagSerializer
from course.models import Category, Course, Tag


class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = CategorySerializer
    filterset_fields = ['title', 'id', 'slug']
    search_fields = ['title', 'id', 'slug']
    ordering_fields = '__all__'
    queryset = Category.objects.all()


class CategorySlugDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    lookup_field = 'slug'
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CourseViewSet(ModelViewSet):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = CourseSerializer
    filterset_fields = ['title', 'id', 'slug', 'language', 'price', 'discount', 'active']
    search_fields = ['title', 'id', 'slug', 'language', 'price', 'discount', 'active']
    ordering_fields = '__all__'
    queryset = Course.objects.all()

    # Overriding save method
    def create(self, request, *args, **kwargs):
        course = request.data  # Get request data
        category_id = course.get('category_id')  # get category_id

        if category_id is None:  # if the user didn't pass category_id throw an error
            error_message = {
                'category_id': ['category_id is required.']
            }
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

        try:  # check if passed category_id is valid
            category = Category.objects.get(pk=category_id)

        # DoesNotExist checks for error
        # ValidationError if pk is in valid uuid format
        except Category.DoesNotExist or ValidationError:
            error_message = {
                'category_id': ['category_id is not valid.']
            }
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

        context = {
            'request': request
        }
        serializer = CourseSerializer(data=course, context=context)

        if serializer.is_valid():
            courseInstance = Course(**serializer.validated_data, category=category)
            courseInstance.save()
            return Response(CourseSerializer(courseInstance, context=context).data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseSlugDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    lookup_field = 'slug'
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class TagViewSet(ModelViewSet):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = TagSerializer
    filterset_fields = ['id', 'tag']
    search_fields = ['id', 'tag']
    ordering_fields = '__all__'
    queryset = Tag.objects.all()

    def create(self, request, *args, **kwargs):
        tag = request.data
        course_id = tag.get('course')
        course = None

        try:
            course = Course.objects.get(pk=course_id)
        except Course.DoesNotExist or ValidationError:
            error_message = {
                'course': ["course_id is invalid!"]
            }
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

        serializer = TagSerializer(data=tag)

        if serializer.is_valid():
            tag = Tag(**serializer.validated_data, course=course)
            tag.save()
            return Response(TagSerializer(tag).data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CoursesByCategoryView(APIView):
    def get(self, request, category_id):
        # courses = Course.objects.filter(category_id=Category(pk=category_id))
        try:
            courses = Course.objects.filter(category_id=category_id)
        except ValidationError:
            error_message = {
                'category': ["category_id is invalid!"]
            }
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
