from django.db import models
from teachers.models import Teacher


class Course(models.Model):

    course_id = models.CharField(
        max_length=20,
        unique=True
    )

    course_code = models.CharField(
        max_length=20,
        unique=True
    )

    course_name = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    credits = models.PositiveIntegerField(
        default=3
    )

    duration = models.CharField(
        max_length=50
    )

    created_date = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.course_code} - {self.course_name}"