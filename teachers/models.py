from django.db import models


class Teacher(models.Model):

    teacher_id = models.CharField(
        max_length=20,
        unique=True
    )

    first_name = models.CharField(
        max_length=50
    )

    last_name = models.CharField(
        max_length=50
    )

    email = models.EmailField(
        unique=True
    )

    phone = models.CharField(
        max_length=15
    )

    subject = models.CharField(
        max_length=100
    )

    address = models.CharField(
        max_length=200
    )

    joined_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"