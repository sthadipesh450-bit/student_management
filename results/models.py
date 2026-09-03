from django.db import models
from students.models import Student
from subjects.models import Subject


class Result(models.Model):

    EXAM_CHOICES = [
        ('First Terminal', 'First Terminal'),
        ('Second Terminal', 'Second Terminal'),
        ('Final Examination', 'Final Examination'),
    ]

    result_id = models.CharField(max_length=20, unique=True)

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )

    exam_type = models.CharField(
        max_length=50,
        choices=EXAM_CHOICES
    )

    marks = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    full_marks = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=100
    )

    grade = models.CharField(
        max_length=5,
        blank=True
    )

    gpa = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        blank=True,
        null=True
    )

    remarks = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    result_date = models.DateField(
        auto_now_add=True
    )

    def calculate_grade(self):

        percentage = (float(self.marks) / float(self.full_marks)) * 100

        if percentage >= 90:
            return 'A+'
        elif percentage >= 80:
            return 'A'
        elif percentage >= 70:
            return 'B+'
        elif percentage >= 60:
            return 'B'
        elif percentage >= 50:
            return 'C+'
        elif percentage >= 40:
            return 'C'
        else:
            return 'F'

    def calculate_gpa(self):

        percentage = (float(self.marks) / float(self.full_marks)) * 100

        if percentage >= 90:
            return 4.0
        elif percentage >= 80:
            return 3.6
        elif percentage >= 70:
            return 3.2
        elif percentage >= 60:
            return 2.8
        elif percentage >= 50:
            return 2.4
        elif percentage >= 40:
            return 2.0
        else:
            return 0.0

    def save(self, *args, **kwargs):

        self.grade = self.calculate_grade()
        self.gpa = self.calculate_gpa()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student} - {self.subject}"