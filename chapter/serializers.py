from rest_framework.serializers import ModelSerializer

from .models import Chapter, TextChapter, HeadingChapter, VideoChapter, LinkChapter


class ChapterSerializer(ModelSerializer):
    class Meta:
        model = Chapter
        fields = "__all__"


class TextChapterSerializer(ModelSerializer):
    class Meta:
        model = TextChapter
        fields = "__all__"


class HeadingChapterSerializer(ModelSerializer):
    class Meta:
        model = HeadingChapter
        fields = "__all__"


class VideoChapterSerializer(ModelSerializer):
    class Meta:
        model = VideoChapter
        fields = "__all__"


class LinkChapterSerializer(ModelSerializer):
    class Meta:
        model = LinkChapter
        fields = "__all__"
