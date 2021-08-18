from django.contrib import admin


from chapter.models import Chapter


# Register your models here.
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['course', 'chapter_type', 'index', 'child_chapters']


admin.site.register(Chapter, ChapterAdmin)
