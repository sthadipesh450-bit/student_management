from django import forms

from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'course_id',
            'course_code',
            'course_name',
            'description',
            'teacher',
            'subject',
            'credits',
            'duration',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
