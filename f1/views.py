from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from coreapp.models import Group, Membership, Person


def home(request):
    return HttpResponse(
        """
    <h1>F1 home page</h1>
    Persons: <a href="persons/">List</a> |
    <a href="persons/add/">Add</a>
    """
    )


def person_list(request):
    persons = Person.objects.all()
    return render(request, "f1/person_list.html", {"person_list": persons})


def person_add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        person = Person.objects.create(name=name)
        return redirect("f1:person-detail", pk=person.pk)
    else:
        return render(request, "f1/person_form.html")


def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    return HttpResponse(f"Person name: {person}")


def person_change(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        person.name = request.POST.get("name")
        person.save()
        return redirect("f1:person-detail", pk=person.pk)

    return render(request, "f1/person_change.html", {"name": person.name})


def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        person.delete()
        return redirect("f1:person-list")

    return render(request, "f1/person_delete.html", {"name": person.name})
