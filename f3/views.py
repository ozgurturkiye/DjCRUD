# F3 views.py
from django.shortcuts import get_object_or_404, redirect, render

from coreapp.models import Group, Membership, Person

from .forms import PersonForm


def home(request):
    return render(request, "f3/home.html")


def person_list(request):
    persons = Person.objects.all()
    return render(request, "f3/person_list.html", {"person_list": persons})


def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request, "f3/person_detail.html", {"person": person})


def person_add(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save()
            return redirect("f3:person-detail", pk=person.pk)
    else:
        form = PersonForm()

    return render(request, "f3/person_form.html", {"form": form})


def person_change(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        # Create a form to edit an existing Person, but use
        # POST data to populate the form.
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect("f3:person-detail", pk=person.pk)
    else:
        form = PersonForm(instance=person)

    return render(request, "f3/person_change.html", {"form": form})


def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        person.delete()
        return redirect("f3:person-list")

    return render(request, "f3/person_delete.html", {"name": person.name})
