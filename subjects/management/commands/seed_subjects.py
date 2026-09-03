from random import choice

from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from subjects.models import Subject


class Command(BaseCommand):
    help = "Create sample subject records using Faker."

    def add_arguments(self, parser):
        parser.add_argument("--count", type=int, default=10, help="Number of subjects to create (default: 10).")

    def handle(self, *args, **options):
        count = options["count"]
        if count < 1:
            raise CommandError("--count must be at least 1.")

        fake = Faker()
        departments = ["Computer Science", "Business", "Mathematics", "Humanities", "Engineering"]
        used_ids = set(Subject.objects.values_list("subject_id", flat=True))
        used_codes = set(Subject.objects.values_list("subject_code", flat=True))
        subjects = []
        number = 1
        while len(subjects) < count:
            subject_id = f"SUB{number:04d}"
            subject_code = f"{choice(['CSC', 'BUS', 'MAT', 'ENG', 'HUM'])}{number:03d}"
            if subject_id in used_ids or subject_code in used_codes:
                number += 1
                continue
            department = choice(departments)
            subjects.append(Subject(subject_id=subject_id, subject_code=subject_code, subject_name=fake.catch_phrase().title(), description=fake.paragraph(nb_sentences=3), credits=choice([2, 3, 3, 4]), semester=f"Semester {choice(range(1, 9))}", department=department))
            used_ids.add(subject_id)
            used_codes.add(subject_code)
            number += 1
        Subject.objects.bulk_create(subjects)
        self.stdout.write(self.style.SUCCESS(f"Created {len(subjects)} sample subjects."))
