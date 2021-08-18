from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework import status

from chapter.models import (
    Chapter,
    TextChapter,
    HeadingChapter,
    VideoChapter,
    LinkChapter,
    chapter_choices,
    chapter_choises_description,
    video_platform_choises,
)
from chapter.serializers import (
    ChapterSerializer,
    TextChapterSerializer,
    HeadingChapterSerializer,
    VideoChapterSerializer,
    LinkChapterSerializer,
)


@api_view(["GET"])
def chapter_types_view(request):
    def SearchDescription(id):
        for (
            _id,
            description,
        ) in chapter_choises_description:  # Cannot use id twice hence _id
            if id == _id:
                return description

    types = map(
        lambda e: dict(id=e[0], type=e[1], description=SearchDescription(e[0])),
        chapter_choices,
    )
    return Response(types)


@api_view(["GET"])
def video_platform_view(request):
    platform = map(lambda e: dict(id=e[0], platform=e[1]), video_platform_choises)
    return Response(platform)


class ChapterListView(ListAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    ordering = ["index"]
