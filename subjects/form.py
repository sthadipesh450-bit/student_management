from django import forms
from .models import Subject


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = [
            'subject_id',
            'subject_code',
            'subject_name',
            'description',
            'credits',
            'semester',
            'department',
        ]

        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 4
            }),
        }