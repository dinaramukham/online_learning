from django.contrib import admin

from .models import Lesson, Courses


# Register your models here.
@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'content',)
    list_filter = ('title', 'photo', 'content')
    search_fields = ('title', 'photo', 'content')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('courses', 'title', 'photo', 'content', 'link_video')
    list_filter = ('courses', 'title', 'photo', 'content', 'link_video')
    search_fields = ('courses', 'title', 'photo', 'content', 'link_video')