from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import TemplateView

from c2.forms import PersonForm
from coreapp.models import Person


class HomeView(TemplateView):
    template_name = "c2/home.html"


class PersonListView(TemplateView):
    template_name = "c2/person_list.html"

    def get(self, request, *args, **kwargs):
        persons = Person.objects.all()
        return render(request, self.template_name, {"person_list": persons})


class PersonCreateView(TemplateView):
    template_name = "c2/person_form.html"
    form_class = PersonForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            person = form.save()
            return redirect("c2:person-detail", person.pk)

        return render(request, self.template_name, {"form": form})


class PersonDetailView(TemplateView):
    template_name = "c3/person_detail.html"

    def get(self, request, *args, **kwargs):
        person = get_object_or_404(Person, pk=self.kwargs["pk"])
        return render(request, self.template_name, {"person": person})


class PersonChangeView(TemplateView):
    template_name = "c2/person_change.html"
    form_class = PersonForm

    def get(self, request, *args, **kwargs):
        person = get_object_or_404(Person, pk=self.kwargs["pk"])
        form = self.form_class(instance=person)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            person = form.save()
            return redirect("c2:person-detail", person.pk)
        return render(request, self.template_name, {"form": form})


class PersonDeleteView(TemplateView):
    template_name = "c2/person_delete.html"

    def get(self, request, *args, **kwargs):
        person = get_object_or_404(Person, pk=self.kwargs["pk"])
        return render(request, self.template_name, {"person": person})

    def post(self, request, *args, **kwargs):
        person = get_object_or_404(Person, pk=self.kwargs["pk"])
        person.delete()
        return redirect("c2:person-list")
