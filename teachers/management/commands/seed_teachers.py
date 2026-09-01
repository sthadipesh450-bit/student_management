from random import choice

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from faker import Faker

from teachers.models import Teacher


class Command(BaseCommand):
    help = "Create sample teacher records using Faker."

    def add_arguments(self, parser):
        parser.add_argument(
            "--count",
            type=int,
            default=10,
            help="Number of sample teachers to create (default: 10).",
        )

    def handle(self, *args, **options):
        count = options["count"]
        if count < 1:
            raise CommandError("--count must be at least 1.")

        fake = Faker()
        subjects = [
            "Mathematics",
            "Science",
            "English",
            "Computer Science",
            "Social Studies",
            "Physics",
            "Chemistry",
        ]

        teachers = []
        for _ in range(count):
            teachers.append(
                Teacher(
                    teacher_id=f"TCH{fake.unique.numerify(text='#####')}",
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    email=fake.unique.email(),
                    phone=fake.numerify(text="98########"),
                    subject=choice(subjects),
                    address=fake.address(),
                    joined_date=fake.date_between(
                        start_date="-10y", end_date=timezone.localdate()
                    ),
                )
            )

        Teacher.objects.bulk_create(teachers)
        self.stdout.write(
            self.style.SUCCESS(f"Created {len(teachers)} sample teachers.")
        )
