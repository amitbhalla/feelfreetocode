from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, CourseViewSet, TagViewSet, CourseSlugDetailView, CategorySlugDetailView

# Router setup
category_router = DefaultRouter()
category_router.register('', CategoryViewSet, basename='category')

course_router = DefaultRouter()
course_router.register('', CourseViewSet, basename='course')

tag_router = DefaultRouter()
tag_router.register('', TagViewSet, basename='tag')

# api/courses
urlpatterns = [
    path('tags/', include(tag_router.urls)),
    path('categories/slug/<slug:slug>', CategorySlugDetailView.as_view(), name='category-detail-by-slug'),
    path('categories/', include(category_router.urls)),
    path('slug/<slug:slug>', CourseSlugDetailView.as_view(), name='course-detail-by-slug'),
    path('', include(course_router.urls)),
]
