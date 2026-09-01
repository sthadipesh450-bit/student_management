from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)

from .models import Teacher
from .forms import TeacherForm


class TeacherListView(ListView):

    model = Teacher

    template_name = 'teacher_list.html'

    context_object_name = 'teachers'


class TeacherDetailView(DetailView):

    model = Teacher

    template_name = 'teacher_detail.html'

    context_object_name = 'teacher'


class TeacherCreateView(CreateView):

    model = Teacher

    form_class = TeacherForm

    template_name = 'teacher_form.html'

    success_url = reverse_lazy('teacher_list')


class TeacherUpdateView(UpdateView):

    model = Teacher

    form_class = TeacherForm

    template_name = 'teacher_form.html'

    success_url = reverse_lazy('teacher_list')


class TeacherDeleteView(DeleteView):

    model = Teacher

    template_name = 'teacher_confirm_delete.html'

    success_url = reverse_lazy('teacher_list')
