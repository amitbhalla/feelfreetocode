from django.urls import path
from .views import chapter_types_view, video_platform_view


# api/chapters/
urlpatterns = [
    path('chapter-types/', chapter_types_view, name='chapter-type-view'),
    path('video-platforms/', video_platform_view, name='video-platform-listview'),
]
