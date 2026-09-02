from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import CourseForm
from .models import Course


class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'
    context_object_name = 'courses'
    ordering = ['course_code']


class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'
    context_object_name = 'course'


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'course_form.html'
    success_url = reverse_lazy('course_list')


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'course_form.html'
    success_url = reverse_lazy('course_list')


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'course_confirm_delete.html'
    success_url = reverse_lazy('course_list')
