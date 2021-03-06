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
    chapter = serializers.UUIDField(
        required=False
    )  # Because user will not send this. We will generate this

    class Meta:
        model = TextChapter
        fields = "__all__"

    # used for removing what API view displays
    def to_representation(self, instance):
        original_object = super().to_representation(instance)
        original_object.pop("chapter")
        return original_object


class HeadingChapterSerializer(ModelSerializer):
    chapter = serializers.UUIDField(
        required=False
    )  # Because user will not send this. We will generate this

    class Meta:
        model = HeadingChapter
        fields = "__all__"

    # used for removing what API view displays
    def to_representation(self, instance):
        original_object = super().to_representation(instance)
        original_object.pop("chapter")
        return original_object


class VideoChapterSerializer(ModelSerializer):
    chapter = serializers.UUIDField(
        required=False
    )  # Because user will not send this. We will generate this

    class Meta:
        model = VideoChapter
        fields = "__all__"

    # used for removing what API view displays
    def to_representation(self, instance):
        original_object = super().to_representation(instance)
        original_object.pop("chapter")
        return original_object


class LinkChapterSerializer(ModelSerializer):
    chapter = serializers.UUIDField(
        required=False
    )  # Because user will not send this. We will generate this

    class Meta:
        model = LinkChapter
        fields = "__all__"

    # used for removing what API view displays
    def to_representation(self, instance):
        original_object = super().to_representation(instance)
        original_object.pop("chapter")
        return original_object


# This class is created because we cannot refer to ChapterSerializer inside ChapterSerializer
# Which is what we would use to show nested serializer
class ChildChapterSerializer(ModelSerializer):
    index = serializers.IntegerField(required=False)
    text_chapter = TextChapterSerializer(read_only=True)
    heading_chapter = HeadingChapterSerializer(read_only=True)
    video_chapter = VideoChapterSerializer(read_only=True)
    link_chapter = LinkChapterSerializer(read_only=True)

    class Meta:
        model = Chapter
        fields = "__all__"


class ChapterSerializer(ModelSerializer):
    index = serializers.IntegerField(required=False)

    # Read only since we only use these for display
    text_chapter = TextChapterSerializer(read_only=True)
    heading_chapter = HeadingChapterSerializer(read_only=True)
    video_chapter = VideoChapterSerializer(read_only=True)
    link_chapter = LinkChapterSerializer(read_only=True)
    # End

    # Nested serializer to show child chapter inside parent chapter
    child_chapters = serializers.SerializerMethodField()
    # End

    class Meta:
        model = Chapter
        fields = "__all__"

    # This function is basically used for sorting child chapters by index
    def get_child_chapters(self, instance):
        childs = instance.child_chapters.all().order_by("index")
        serializer = ChildChapterSerializer(childs, many=True)
        print("get - childs:", serializer.data)
        return serializer.data

    # End

    def handle_textchapter(self, data):
        text_chapter_raw = data.get("text_chapter")
        if not text_chapter_raw:
            raise ValidationError({"text_chapter": "text_chapter is required"})
        text_chapter_serializer = TextChapterSerializer(data=text_chapter_raw)
        if text_chapter_serializer.is_valid():
            return TextChapter(**text_chapter_serializer._validated_data)
        else:
            raise ValidationError(
                {"text_chapter": text_chapter_serializer.errors}
            )

    def handle_headingchapter(self, data):
        heading_chapter_raw = data.get("heading_chapter")
        if not heading_chapter_raw:
            raise ValidationError(
                {"heading_chapter": "heading_chapter is required"}
            )
        heading_chapter_serializer = HeadingChapterSerializer(
            data=heading_chapter_raw
        )
        if heading_chapter_serializer.is_valid():
            return HeadingChapter(**heading_chapter_serializer._validated_data)
        else:
            raise ValidationError(
                {"heading_chapter": heading_chapter_serializer.errors}
            )

    def handle_videochapter(self, data):
        video_chapter_raw = data.get("video_chapter")
        if not video_chapter_raw:
            raise ValidationError(
                {"video_chapter": "video_chapter is required"}
            )
        video_chapter_serializer = VideoChapterSerializer(
            data=video_chapter_raw
        )
        if video_chapter_serializer.is_valid():
            return VideoChapter(**video_chapter_serializer._validated_data)
        else:
            raise ValidationError(
                {"video_chapter": video_chapter_serializer.errors}
            )

    def handle_linkchapter(self, data):
        link_chapter_raw = data.get("link_chapter")
        if not link_chapter_raw:
            raise ValidationError({"link_chapter": "link_chapter is required"})
        link_chapter_serializer = LinkChapterSerializer(data=link_chapter_raw)
        if link_chapter_serializer.is_valid():
            return LinkChapter(**link_chapter_serializer._validated_data)
        else:
            raise ValidationError(
                {"link_chapter": link_chapter_serializer.errors}
            )

    def create(self, validated_data):
        data = self.context.get("request").data
        chapter_type = data.get("chapter_type")
        chapter_type_object = None

        if chapter_type == "T":
            chapter_type_object = self.handle_textchapter(data)
        elif chapter_type == "H":
            chapter_type_object = self.handle_headingchapter(data)
        elif chapter_type == "V":
            chapter_type_object = self.handle_videochapter(data)
        elif chapter_type == "L":
            chapter_type_object = self.handle_linkchapter(data)

        # Fetch the chapter objject
        # Get the total parent chapter i.e. those who do not have an index
        # Add one to them and set that as the new index
        chapter = Chapter(**validated_data)
        course = chapter.course
        parent_chapter = validated_data.get("parent_chapter")

        if chapter.parent_chapter is None:
            last_index_parent_chapter = Chapter.objects.filter(
                course=course, parent_chapter=None
            ).count()
            # Save order
            # Save the Chapter first
            # Then save the Link/Heading/Text/Video Chapter
            chapter.index = last_index_parent_chapter + 1
            chapter.save()
            chapter_type_object.chapter = chapter
            chapter_type_object.save()
        else:
            # Save order
            # Save the Chapter first
            # Then save the Link/Heading/Text/Video Chapter
            total_childs = Chapter.objects.filter(
                parent_chapter=parent_chapter
            ).count()
            print("*" * 100)
            chapter.index = total_childs + 1
            print(
                "total_childs:", total_childs, " chapter.index", chapter.index
            )
            chapter.save()
            chapter_type_object.chapter = chapter
            chapter_type_object.save()

        return chapter
