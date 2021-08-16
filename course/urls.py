from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, CourseViewSet, TagViewSet

# Router setup
category_router = DefaultRouter()
category_router.register('', CategoryViewSet, basename='category')

course_router = DefaultRouter()
course_router.register('', CourseViewSet, basename='course')

tag_router = DefaultRouter()
tag_router.register('', TagViewSet, basename='tag')


urlpatterns = [
    path('categories/', include(category_router.urls)),
    path('courses/', include(course_router.urls)),
    path('tags/', include(tag_router.urls)),
]
