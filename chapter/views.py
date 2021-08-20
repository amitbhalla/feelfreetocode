import uuid

from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework import status

from course.models import Course
from chapter.models import (
    Chapter,
    chapter_choices,
    chapter_choises_description,
    video_platform_choises,
)
from chapter.serializers import ChapterSerializer
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


class ChapterListView(ListAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    ordering = ["index"]

    def get(self, request, *args, **kwargs):
        course = self.kwargs.get("course")
        try:
            uuid.UUID(course)
        except ValueError:
            return Response(
                {"course_id": ["Course_id is not a valid UUID format!"]},
                status=status.HTTP_400_BAD_REQUEST,
            )  # Using response become Django doesn't have a native ValueError
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        course = self.kwargs.get("course")
        try:
            query = Chapter.objects.filter(
                parent_chapter=None, course=Course.objects.get(pk=course)
            )
        except Course.DoesNotExist:
            raise ValidationError({"course_id": ["Invalid Course ID!"]})
        return query


class ChapterCreateView(CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

    def get_serializer(self, *args, **kwargs):
        context = {"request": self.request}
        request = self.request
        serializer = self.serializer_class(data=request.data, context=context)
        serializer.is_valid()
        return serializer
