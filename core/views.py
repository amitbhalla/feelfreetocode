from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request):
    response = {
        'API ROOT': reverse('api_root', request=request),

        'Courses': {
            'Course List': reverse('course:course-list', request=request),
            'Course Detail': reverse('course:course-detail', args={'pk': 'pk'}, request=request),
            'Course Detail by Slug': reverse('course:course-detail-by-slug', args={'slug': 'slug'}, request=request),
        },

        'Categories': {
            'Category List': reverse('course:category-list', request=request),
            'Category Detail': reverse('course:category-detail', args={'pk': 'pk'}, request=request),
        },

        'Tags': {
            'Course List': reverse('course:tag-list', request=request),
            'Course Detail': reverse('course:tag-detail', args={'pk': 'pk'}, request=request),
        },
    }
    return Response(response)
