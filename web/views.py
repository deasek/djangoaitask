from django.core.exceptions import ValidationError
from django.urls import reverse
from django.views.generic import DetailView, FormView

from core.models import Summary
from web.forms import InputForm


class AddTextView(FormView):
    template_name = 'web/add_text.html'
    form_class = InputForm
    summary = None

    def get_success_url(self):
        return reverse('web:summary-view', kwargs={
            'pk': self.summary.id
        })

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        try:
            self.summary = Summary.parse_input_file(cleaned_data['input_file'])
        except Exception:
            raise ValidationError('Invalid data')
        return super().form_valid(form)


class SummaryDetailView(DetailView):
    template_name = 'web/summary.html'
    model = Summary

    def get_queryset(self):
        return super().get_queryset().prefetch_related('chunks')

