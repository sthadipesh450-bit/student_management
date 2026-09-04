from django.views.generic import TemplateView

from students.models import Student
from attendance.models import Attendance
from courses.models import Course
from subjects.models import Subject
from teachers.models import Teacher


class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['total_students'] = Student.objects.count()
        context['total_attendance'] = Attendance.objects.count()
        context['total_courses'] = Course.objects.count()
        context['total_subjects'] = Subject.objects.count()
        context['total_teachers'] = Teacher.objects.count()

        context['present_count'] = Attendance.objects.filter(status='Present').count()
        context['absent_count'] = Attendance.objects.filter(status='Absent').count()
        context['late_count'] = Attendance.objects.filter(status='Late').count()
        context['recent_attendance'] = Attendance.objects.select_related(
            'student'
        ).order_by('-date', '-id')[:5]
        context['recent_students'] = Student.objects.order_by('-id')[:5]

        return context
