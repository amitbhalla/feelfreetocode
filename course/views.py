from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from course.serializers import CategorySerializer, CourseSerializer, TagSerializer
from course.models import Category, Course, Tag


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseSlugDetailView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class TagViewSet(ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
