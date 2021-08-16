from django.contrib import admin
from .models import Course, Category, Tag


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['slug', 'title', 'id']


class CourseAdmin(admin.ModelAdmin):
    list_editable = ['active']
    list_display = ['title', 'discount', 'active', 'id']
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):
    list_display = ['tag', 'course', 'id']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Tag, TagAdmin)
