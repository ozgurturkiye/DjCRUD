from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import TemplateView

from c1.forms import NameForm
from coreapp.models import Person


class HomeView(TemplateView):
    template_name = "c1/home.html"


class PersonListView(View):
    def get(self, request, *args, **kwargs):
        persons = Person.objects.all()
        return render(request, "c1/person_list.html", {"person_list": persons})


class PersonDetailView(View):
    def get(self, request, *args, **kwargs):
        person = get_object_or_404(Person, pk=self.kwargs["pk"])
        return render(request, "c1/person_detail.html", {"person": person})


class PersonCreateView(View):
    form_class = NameForm
    template_name = "c1/person_form.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            person = Person.objects.create(name=form.cleaned_data["name"])
            return redirect("c1:person-detail", pk=person.pk)

        return render(request, self.template_name, {"form": form})


class PersonChangeView(View):
    form_class = NameForm
    template_name = "c1/person_change.html"

    def get(self, request, *args, **kwargs):
        person = get_object_or_404(Person, pk=self.kwargs["pk"])
        form = self.form_class(initial={"name": person.name})
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        person = get_object_or_404(Person, pk=self.kwargs["pk"])
        form = self.form_class(request.POST, initial={"name": person.name})
        if form.is_valid():
            person.name = form.cleaned_data["name"]
            person.save()
            return redirect("c1:person-detail", pk=self.kwargs["pk"])

        return render(request, self.template_name, {"form": form})


class PersonDeleteView(View):
    def get(self, request, *args, **kwargs):
        person = get_object_or_404(Person, pk=self.kwargs["pk"])
        return render(request, "c1/person_delete.html", {"person": person})

    def post(self, request, *args, **kwargs):
        person = get_object_or_404(Person, pk=self.kwargs["pk"])
        person.delete()
        return redirect("c1:person-list")
