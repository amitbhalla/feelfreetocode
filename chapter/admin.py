from django.contrib import admin


from chapter.models import (
    Chapter,
    TextChapter,
    HeadingChapter,
    VideoChapter,
    LinkChapter,
)
from chapter.forms import TextChapterForm


# Register your models here.
class ChapterAdmin(admin.ModelAdmin):
    list_display = ["course", "chapter_type", "index", "child_chapters"]


class TextChapterAdmin(admin.ModelAdmin):
    list_display = ["chapter", "title"]
    form = TextChapterForm


class HeadingChapterAdmin(admin.ModelAdmin):
    list_display = ["chapter", "title"]


class VideoChapterAdmin(admin.ModelAdmin):
    list_display = ["chapter", "title"]


class LinkChapterAdmin(admin.ModelAdmin):
    list_display = ["chapter", "title"]


admin.site.register(Chapter, ChapterAdmin)
admin.site.register(TextChapter, TextChapterAdmin)
admin.site.register(HeadingChapter, HeadingChapterAdmin)
admin.site.register(VideoChapter, VideoChapterAdmin)
admin.site.register(LinkChapter, LinkChapterAdmin)
