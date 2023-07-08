from django.urls import reverse, reverse_lazy
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apis1.serializers import PersonSerializer
from coreapp.models import Person


@api_view(["GET"])
def home(request):
    data = {
        "person-list": request.build_absolute_uri(reverse("apis1:person-list")),
        "person-detail": request.get_full_path() + "{lookup}/",
    }
    return Response(data)


@api_view(["GET", "POST"])
def person_list(request):
    """
    List all code persons, or create a new person.
    """
    if request.method == "GET":
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def person_detail(request, pk):
    """
    Retrieve, update or delete a person.
    """
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
