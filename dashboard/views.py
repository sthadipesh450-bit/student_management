from django.views.generic import TemplateView

from students.models import Student
from attendance.models import Attendance


class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['total_students'] = Student.objects.count()
        context['total_attendance'] = Attendance.objects.count()

        return context