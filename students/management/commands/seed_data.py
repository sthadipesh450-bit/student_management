from datetime import timedelta
from random import choice, randint

from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker

from attendance.models import Attendance
from students.models import Student


class Command(BaseCommand):
    help = "Create sample students and attendance records using Faker."

    def add_arguments(self, parser):
        parser.add_argument(
            "--students",
            type=int,
            default=15,
            help="Number of sample students to create (default: 15).",
        )

    def handle(self, *args, **options):
        if options["students"] < 1:
            self.stderr.write("--students must be at least 1.")
            return

        fake = Faker()
        created_students = []

        for _ in range(options["students"]):
            student = Student.objects.create(
                student_id=f"STU{fake.unique.bothify(text='#####')}",
                name=fake.name(),
                age=randint(16, 28),
                email=fake.unique.email(),
                phone=fake.numerify(text="98########"),
                course=choice(
                    [
                        "Computer Science",
                        "Business Studies",
                        "Information Technology",
                        "Mathematics",
                        "Engineering",
                    ]
                ),
                address=fake.address(),
            )
            created_students.append(student)

        attendance_records = []
        for student in created_students:
            for days_ago in range(5):
                status = choice(["Present", "Present", "Present", "Late", "Absent"])
                attendance_records.append(
                    Attendance(
                        student=student,
                        date=timezone.localdate() - timedelta(days=days_ago),
                        status=status,
                        remarks="" if status == "Present" else fake.sentence(nb_words=5),
                    )
                )

        Attendance.objects.bulk_create(attendance_records)
        self.stdout.write(
            self.style.SUCCESS(
                f"Created {len(created_students)} students and "
                f"{len(attendance_records)} attendance records."
            )
        )
