from django.views.generic import TemplateView
from django.db.models import Avg
from django.utils import timezone

from students.models import Student
from attendance.models import Attendance
from courses.models import Course
from subjects.models import Subject
from teachers.models import Teacher
from results.models import Result


class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['total_students'] = Student.objects.count()
        context['total_attendance'] = Attendance.objects.count()
        context['total_courses'] = Course.objects.count()
        context['total_subjects'] = Subject.objects.count()
        context['total_teachers'] = Teacher.objects.count()
        context['total_results'] = Result.objects.count()

        context['present_count'] = Attendance.objects.filter(status='Present').count()
        context['absent_count'] = Attendance.objects.filter(status='Absent').count()
        context['late_count'] = Attendance.objects.filter(status='Late').count()
        context['average_gpa'] = Result.objects.aggregate(average=Avg('gpa'))['average']
        context['failed_results'] = Result.objects.filter(grade='F').count()

        today = timezone.localdate()
        context['today_present'] = Attendance.objects.filter(
            date=today, status='Present'
        ).count()
        context['today_absent'] = Attendance.objects.filter(
            date=today, status='Absent'
        ).count()
        context['today_late'] = Attendance.objects.filter(
            date=today, status='Late'
        ).count()
        context['attendance_rate'] = (
            round((context['present_count'] / context['total_attendance']) * 100, 1)
            if context['total_attendance']
            else 0
        )
        context['recent_attendance'] = Attendance.objects.select_related(
            'student'
        ).order_by('-date', '-id')[:5]
        context['recent_students'] = Student.objects.order_by('-id')[:5]
        context['recent_results'] = Result.objects.select_related(
            'student', 'subject'
        ).order_by('-result_date', '-id')[:5]

        return context
