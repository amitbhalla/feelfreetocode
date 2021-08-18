from rest_framework.response import Response
from rest_framework.decorators import api_view
from chapter.models import chapter_choices, chapter_choises_description, video_platform_choises


@api_view(['GET'])
def chapter_types_view(request):

    def SearchDescription(id):
        for _id, description in chapter_choises_description:  # Cannot use id twice hence _id
            if id == _id:
                return description

    def ChangeToDict(chapter_type):
        id, type = chapter_type
        return {
            'id': id,
            'type': type,
            'description': SearchDescription(id),
        }
    types = map(ChangeToDict, chapter_choices)
    return Response(types)


@api_view(['GET'])
def video_platform_view(request):

    def ChangeToDict(video_platforms):
        id, type = video_platforms
        return {
            'id': id,
            'platform': type,
        }
    platform = map(ChangeToDict, video_platform_choises)
    return Response(platform)
