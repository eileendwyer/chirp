from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from main.models import Chirp

class IndexView(TemplateView):
    template_name = "index.html"
    model = Chirp

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["amount"] = Chirp.objects.all().count()
        return context
