from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    ListCreateAPIView,
)
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
from core.permissions import IsAdminUserOrReadOnly


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
        lambda e: dict(
            id=e[0], type=e[1], description=SearchDescription(e[0])
        ),
        chapter_choices,
    )
    return Response(types)


@api_view(["GET"])
def video_platform_view(request):
    platform = map(
        lambda e: dict(id=e[0], platform=e[1]), video_platform_choises
    )
    return Response(platform)


class ChapterListCreateView(ListCreateAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

    def get_serializer(self, *args, **kwargs):
        if self.request.method == "POST":
            context = {"request": self.request}
            request = self.request
            return self.serializer_class(data=request.data, context=context)
        return self.serializer_class(self.queryset.all(), many=True)
