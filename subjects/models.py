from django.db import models


class Subject(models.Model):
    subject_id = models.CharField(max_length=20, unique=True)
    subject_code = models.CharField(max_length=20, unique=True)
    subject_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    credits = models.PositiveIntegerField(default=3)
    semester = models.CharField(max_length=20)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.subject_code} - {self.subject_name}"
