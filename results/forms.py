from django import forms
from .models import Result


class ResultForm(forms.ModelForm):

    class Meta:
        model = Result

        fields = [
            'result_id',
            'student',
            'subject',
            'exam_type',
            'marks',
            'full_marks',
            'remarks',
        ]

        widgets = {
            'remarks': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Enter remarks'
            }),
        }