from django.core.exceptions import ValidationError
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
    queryset = Category.objects.all()


class CategorySlugDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    lookup_field = 'slug'
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CourseViewSet(ModelViewSet):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def create(self, request, *args, **kwargs):
        course = request.data  # Get request data
        category_id = course.get('category_id')  # get category_id

        if category_id is None:  # if the user didn't pass category_id throw an error
            error_message = {
                'category_id': ['category_id is required.']
            }
            return Response(error_message)

        try:  # check if passed category_id is valid
            category = Category.objects.get(pk=category_id)

        # DoesNotExist checks for error
        # ValidationError if pk is in valid uuid format
        except Category.DoesNotExist or ValidationError:
            error_message = {
                'category_id': ['category_id is not valid.']
            }
            return Response(error_message)

        context = {
            'request': request
        }
        serializer = CourseSerializer(data=course, context=context)

        if serializer.is_valid():
            courseInstance = Course(**serializer.validated_data, category=category)
            courseInstance.save()
            return Response(CourseSerializer(courseInstance, context=context).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseSlugDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    lookup_field = 'slug'
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class TagViewSet(ModelViewSet):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = TagSerializer
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
            return Response(error_message)

        serializer = TagSerializer(data=tag)

        if serializer.is_valid():
            tag = Tag(**serializer.validated_data, course=course)
            tag.save()
            return Response(TagSerializer(tag).data)
        else:
            return Response(serializer.errors)
