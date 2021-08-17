from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from core.permissions import IsAdminUserOrReadOnly
from course.serializers import CategorySerializer, CourseSerializer, TagSerializer
from course.models import Category, Course, Tag


class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategorySlugDetailView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CourseViewSet(ModelViewSet):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseSlugDetailView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class TagViewSet(ModelViewSet):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
