# c3 views.py
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from coreapp.models import Person


class HomeView(TemplateView):
    template_name = "c3/home.html"


class PersonListView(ListView):
    model = Person
    template_name = "c3/person_list.html"


class PersonDetailView(DetailView):
    model = Person
    template_name = "c3/person_detail.html"


class PersonCreateView(CreateView):
    model = Person
    template_name = "c3/person_form.html"
    fields = ["name"]
    success_url = reverse_lazy("c3:person-list")


class PersonUpdateView(UpdateView):
    model = Person
    template_name = "c3/person_form.html"
    success_url = reverse_lazy("c3:person-list")
    fields = ["name"]


class PersonDeleteView(DeleteView):
    model = Person
    template_name = "c3/person_confirm_delete.html"
    success_url = reverse_lazy("c3:person-list")
