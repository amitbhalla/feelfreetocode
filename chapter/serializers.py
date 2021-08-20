from django.core.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import (
    Chapter,
    TextChapter,
    HeadingChapter,
    VideoChapter,
    LinkChapter,
)


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


class ChapterSerializer(ModelSerializer):
    index = serializers.IntegerField(required=False)

    class Meta:
        model = Chapter
        fields = "__all__"

    def create(self, validated_data):
        data = self.context.get("request").data
        chapter_type = data.get("chapter_type")

        if chapter_type == "H":
            heading_chapter_raw = data.get("heading_chapter")
            if not heading_chapter_raw:
                raise ValidationError(
                    {"heading_chapter": "heading_chapter is required"}
                )
            heading_chapter_serializer = HeadingChapterSerializer(
                data=heading_chapter_raw
            )
            if heading_chapter_serializer.is_valid():
                print("-" * 100)
                print(heading_chapter_serializer.validated_data)
            else:
                raise ValidationError(
                    {"heading_chapter": heading_chapter_serializer.errors}
                )

        return Chapter()
