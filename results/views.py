from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)

from .models import Result
from .forms import ResultForm


class ResultListView(ListView):

    model = Result

    template_name = 'results/result_list.html'

    context_object_name = 'results'


class ResultDetailView(DetailView):

    model = Result

    template_name = 'results/result_detail.html'

    context_object_name = 'result'


class ResultCreateView(CreateView):

    model = Result

    form_class = ResultForm

    template_name = 'results/result_form.html'

    success_url = reverse_lazy('result_list')


class ResultUpdateView(UpdateView):

    model = Result

    form_class = ResultForm

    template_name = 'results/result_form.html'

    success_url = reverse_lazy('result_list')


class ResultDeleteView(DeleteView):

    model = Result

    template_name = 'results/result_confirm_delete.html'

    success_url = reverse_lazy('result_list')