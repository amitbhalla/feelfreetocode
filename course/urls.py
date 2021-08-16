from django.urls import path
from .views import test_view, CategoryListView

# api/
urlpatterns = [
    path('test/', test_view, name='test-api'),
    path('categories/', CategoryListView.as_view(), name='course-listview'),
]
