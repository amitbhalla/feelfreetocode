from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request):
    response = {
        'API ROOT': reverse('api_root', request=request),

        'Courses': {
            'Course List': reverse('course:course-list', request=request),
            'Course Detail by PK': reverse('course:course-detail', args=[1], request=request),
            'Course Detail by Slug': reverse('course:course-detail-by-slug', args=['course-slug'], request=request),
        },

        'Categories': {
            'Category List': reverse('course:category-list', request=request),
            'Category Detail by PK': reverse('course:category-detail', args=[1], request=request),
            'Category Detail by Slug': reverse('course:category-detail-by-slug', args=['category-slug'], request=request),
        },

        'Tags': {
            'Course List': reverse('course:tag-list', request=request),
            'Course Detail by PK': reverse('course:tag-detail', args=[1], request=request),
        },
    }
    return Response(response)
