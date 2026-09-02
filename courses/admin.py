from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = (
        'course_id',
        'course_code',
        'course_name',
        'teacher',
        'credits',
        'duration',
        'created_date',
    )

    search_fields = (
        'course_id',
        'course_code',
        'course_name',
    )

    list_filter = (
        'credits',
        'teacher',
    )