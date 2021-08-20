from django.contrib import admin

from chapter.models import (
    Chapter,
    TextChapter,
    HeadingChapter,
    VideoChapter,
    LinkChapter,
)
from chapter.forms import TextChapterForm


class ChapterAdmin(admin.ModelAdmin):
    list_display = [
        "course",
        "chapter_type",
        "index",
        "parent_chapter",
        "id",
    ]
    ordering = ["course", "index"]
    readonly_fields = ("id",)


class TextChapterAdmin(admin.ModelAdmin):
    list_display = ["title", "chapter", "id"]
    ordering = ["chapter", "title"]
    form = TextChapterForm
    readonly_fields = ("id",)


class HeadingChapterAdmin(admin.ModelAdmin):
    list_display = ["title", "chapter", "id"]
    ordering = ["chapter", "title"]
    readonly_fields = ("id",)


class VideoChapterAdmin(admin.ModelAdmin):
    list_display = ["title", "chapter", "id"]
    ordering = ["chapter", "title"]
    readonly_fields = ("id",)


class LinkChapterAdmin(admin.ModelAdmin):
    list_display = ["title", "chapter", "id"]
    ordering = ["chapter", "title"]
    readonly_fields = ("id",)


admin.site.register(Chapter, ChapterAdmin)
admin.site.register(TextChapter, TextChapterAdmin)
admin.site.register(HeadingChapter, HeadingChapterAdmin)
admin.site.register(VideoChapter, VideoChapterAdmin)
admin.site.register(LinkChapter, LinkChapterAdmin)
