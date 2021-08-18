from rest_framework.response import Response
from rest_framework.decorators import api_view
from chapter.models import chapter_choices, chapter_choises_description, video_platform_choises


@api_view(['GET'])
def chapter_types_view(request):

    def SearchDescription(id):
        for _id, description in chapter_choises_description:  # Cannot use id twice hence _id
            if id == _id:
                return description
    types = map(lambda e: dict(id=e[0], type=e[1], description=SearchDescription(e[0])), chapter_choices)
    return Response(types)


@api_view(['GET'])
def video_platform_view(request):
    platform = map(lambda e: dict(id=e[0], platform=e[1]), video_platform_choises)
    return Response(platform)
