from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

from .models import Teacher


class TeacherPageTests(TestCase):
    def test_teacher_list_loads(self):
        response = self.client.get(reverse('teacher_list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher_list.html')

    def test_seed_teachers_command_creates_requested_records(self):
        call_command('seed_teachers', count=3)

        self.assertEqual(Teacher.objects.count(), 3)
