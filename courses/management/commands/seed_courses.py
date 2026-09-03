from random import choice

from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from courses.models import Course
from subjects.models import Subject
from teachers.models import Teacher


class Command(BaseCommand):
    help = "Create sample course records using Faker."

    def add_arguments(self, parser):
        parser.add_argument(
            "--count",
            type=int,
            default=10,
            help="Number of sample courses to create (default: 10).",
        )

    def handle(self, *args, **options):
        count = options["count"]
        if count < 1:
            raise CommandError("--count must be at least 1.")

        fake = Faker()
        teachers = list(Teacher.objects.all())
        available_subjects = list(Subject.objects.all())
        subjects = [
            "Computer Science",
            "Business Studies",
            "Data Analytics",
            "Mathematics",
            "Digital Marketing",
            "Software Engineering",
            "English Literature",
        ]
        courses = []
        used_course_ids = set(Course.objects.values_list("course_id", flat=True))
        used_course_codes = set(Course.objects.values_list("course_code", flat=True))
        course_number = 1

        while len(courses) < count:
            course_id = f"CRS{course_number:04d}"
            subject_name = choice(subjects)
            subject = choice(available_subjects) if available_subjects else None
            course_code = f"{subject_name[:3].upper()}{course_number:03d}"

            if course_id in used_course_ids or course_code in used_course_codes:
                course_number += 1
                continue

            courses.append(
                Course(
                    course_id=course_id,
                    course_code=course_code,
                    course_name=f"Introduction to {subject_name}",
                    description=fake.paragraph(nb_sentences=3),
                    teacher=choice(teachers) if teachers else None,
                    subject=subject,
                    credits=choice([2, 3, 3, 4]),
                    duration=choice(["8 weeks", "12 weeks", "16 weeks", "6 months"]),
                )
            )
            used_course_ids.add(course_id)
            used_course_codes.add(course_code)
            course_number += 1

        Course.objects.bulk_create(courses)
        teacher_message = "assigned to available teachers" if teachers else "without teachers"
        self.stdout.write(
            self.style.SUCCESS(
                f"Created {len(courses)} sample courses {teacher_message}."
            )
        )
