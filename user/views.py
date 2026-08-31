from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.views.generic.edit import FormView


class RegisterView(FormView):
    """Create an account and immediately sign the new user in."""

    template_name = 'registration/register.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('dashboard')
