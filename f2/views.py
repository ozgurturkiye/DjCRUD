# F2 views.py
from django.shortcuts import get_object_or_404, redirect, render

from coreapp.models import Group, Membership, Person

from .forms import NameForm


def home(request):
    return render(request, "f2/home.html")


def person_list(request):
    persons = Person.objects.all()
    return render(request, "f2/person_list.html", {"person_list": persons})


def person_add(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            person = Person.objects.create(name=form.cleaned_data["name"])
            return redirect("f2:person-detail", pk=person.pk)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "f2/person_form.html", {"form": form})


def person_change(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        # form = NameForm(request.POST)
        form = NameForm(request.POST, initial={"name": person.name})
        if form.is_valid() and form.has_changed():
            person.name = form.cleaned_data["name"]
            person.save()
            return redirect("f2:person-detail", pk=person.pk)
    else:
        form = NameForm(initial={"name": person.name})

    return render(request, "f2/person_change.html", {"form": form})


def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request, "f2/person_detail.html", {"person": person})


def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        person.delete()
        return redirect("f2:person-list")

    return render(request, "f2/person_delete.html", {"name": person.name})
