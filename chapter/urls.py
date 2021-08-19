from django.urls import path


from chapter.views import ChapterCreateView, ChapterDetailView, ChapterListView, chapter_types_view, video_platform_view

# base url : api/chapters/
urlpatterns = [
    path('chapter-types/', chapter_types_view, name='chapter-type-view'),
    path('video-platforms/', video_platform_view, name='video-platform-listview'),
    path('', ChapterCreateView.as_view(), name='chapter-createview'),
    path('<str:pk>/', ChapterDetailView.as_view(), name='chapter-detailview'),
    path('course/<str:course>', ChapterListView.as_view(), name='chapter-listview'),
]
