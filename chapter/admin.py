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
    list_display = ["course", "chapter_type", "index"]
    ordering = ["course"]


class TextChapterAdmin(admin.ModelAdmin):
    list_display = ["title", "chapter"]
    ordering = ["chapter"]
    form = TextChapterForm


class HeadingChapterAdmin(admin.ModelAdmin):
    list_display = ["title", "chapter"]
    ordering = ["chapter"]


class VideoChapterAdmin(admin.ModelAdmin):
    list_display = ["title", "chapter"]
    ordering = ["chapter"]


class LinkChapterAdmin(admin.ModelAdmin):
    list_display = ["title", "chapter"]
    ordering = ["chapter"]


admin.site.register(Chapter, ChapterAdmin)
admin.site.register(TextChapter, TextChapterAdmin)
admin.site.register(HeadingChapter, HeadingChapterAdmin)
admin.site.register(VideoChapter, VideoChapterAdmin)
admin.site.register(LinkChapter, LinkChapterAdmin)
