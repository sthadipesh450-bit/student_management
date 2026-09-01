from django import forms
from .models import Teacher


class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher

        fields = [
            'teacher_id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'subject',
            'address',
            'joined_date',
        ]

        widgets = {
            'joined_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }