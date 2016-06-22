from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from main.models import Chirp, StopWord

class IndexView(ListView):
    template_name = "index.html"
    model = Chirp

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["amount"] = Chirp.objects.all().count()
        return context

class ChirpDetailView(DetailView):
    model = Chirp

    def get_queryset(self):
        return Chirp.objects.filter(bird=self.request.user)

class ChirpCreateView(CreateView):
    model = Chirp
    fields = ["body"]
    success_url = "/"

    def form_valid(self, form):
        # if trump/clinton/or sanders in body, add error
        #stop_words = ["trump", "sanders", "clinton"] - don't hardcode - do below
        stop_words = StopWord.objects.all()
        chirp_body = form.cleaned_data["body"].lower()
        for stop_word in stop_words:
        #raise Exception(chirp_body)
            if stop_word.word in chirp_body:
                form.add_error("body", "POLITICAL DISCUSSION REVOKED!")
            return self.form_invalid(form)
            raise Exception("POLITICAL DISCUSSION REVOKED!")

        chirp = form.save(commit=False)
        chirp.bird = self.request.user
        return super().form_valid(form)
