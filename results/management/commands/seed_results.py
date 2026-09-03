from random import choice, randint
from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from results.models import Result
from students.models import Student
from subjects.models import Subject


class Command(BaseCommand):
    help = "Create sample result records."

    def add_arguments(self, parser):
        parser.add_argument("--count", type=int, default=20)

    def handle(self, *args, **options):
        count = options["count"]

        if count < 1:
            raise CommandError("--count must be at least 1.")

        students = list(Student.objects.all())
        subjects = list(Subject.objects.all())

        if not students or not subjects:
            raise CommandError(
                "Create students and subjects before creating results."
            )

        fake = Faker()
        exam_types = [
            "First Terminal",
            "Second Terminal",
            "Final Examination",
        ]

        existing_ids = set(Result.objects.values_list("result_id", flat=True))
        results = []

        for number in range(1, count + 1):
            result_id = f"RES{number:04d}"

            while result_id in existing_ids:
                number += 1
                result_id = f"RES{number:04d}"

            full_marks = 100
            marks = randint(30, full_marks)

            results.append(
                Result(
                    result_id=result_id,
                    student=choice(students),
                    subject=choice(subjects),
                    exam_type=choice(exam_types),
                    marks=marks,
                    full_marks=full_marks,
                    remarks=fake.sentence(nb_words=6),
                )
            )
            existing_ids.add(result_id)

        for result in results:
            result.save()

        self.stdout.write(
            self.style.SUCCESS(f"Created {len(results)} sample results.")
        )