import uuid

from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.permissions import IsAdminUser


from core.permissions import IsAdminUserOrReadOnly
from course.models import Course
from chapter.serializers import ChapterSerializer
from chapter.models import Chapter, chapter_choices, chapter_choises_description, video_platform_choises


@api_view(['GET'])
def chapter_types_view(request):

    def searchDescription(id):
        for _id, description in chapter_choises_description:
            if id == _id:
                return description

    types = map(lambda e: dict(
        id=e[0], type=e[1], description=searchDescription(e[0])), chapter_choices)
    return Response(types)


@api_view(['GET'])
def video_platform_view(request):

    platforms = map(lambda e: dict(
        id=e[0], platform=e[1]), video_platform_choises)
    return Response(platforms)


class ChapterListView(ListAPIView):
    # we wiil add persmission only user who purched this course
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    ordering = ['index']

    def get(self, request, *args, **kwargs):
        try:
            course = self.kwargs.get('course')
            uuid.UUID(course)
        except ValidationError:
            return Response({"course": ["Course id is not valid"]}, status=status.HTTP_400_BAD_REQUEST)
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        course = self.kwargs.get('course')
        return Chapter.objects.filter(parent_chapter=None, course=Course(pk=course))


class ChapterCreateView(CreateAPIView):

    permission_classes = [IsAdminUser]
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

    def get_serializer(self, *args, **kwargs):

        request = self.request
        print(request.data)
        serializer = self.serializer_class(data=request.data, context={"request": request, "full": True})
        serializer.is_valid()
        return serializer


class ChapterDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get(self, request, **kargs):
        chapter_id = kargs.get('pk')
        user = request.user
        try:
            chapter = Chapter.objects.get(pk=chapter_id)
        except Chapter.DoesNotExist or ValidationError:
            return Response(status=404)
        #  user subscribed this course
        # then alwaays return full ojject data
        # add full flag in create Chapter View
        context = {
            "full": chapter.is_preview,
            "request": request
        }

        if user.is_authenticated:
            if (user.is_superuser):
                context['full'] = True
            else:
                context['full'] = chapter.course.is_user_enrolled(user)

        serailizer = ChapterSerializer(chapter, context=context)
        return Response(serailizer.data)
