from rest_framework.response import Response
from rest_framework.decorators import api_view
from chapter.models import chapter_choices, chapter_choises_description


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
