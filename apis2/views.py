# apis2 views.py
from django.http import Http404
from django.urls import reverse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from apis1.serializers import PersonSerializer
from coreapp.models import Person


class Home(APIView):
    def get(self, request):
        data = {
            "person-list": request.build_absolute_uri(reverse("apis2:person-list")),
            "person-detail": request.get_full_path() + "{lookup}/",
        }
        return Response(data)


class PersonList(APIView):
    """
    List all persons, or create a new person.
    """

    def get(self, request):
        snippets = Person.objects.all()
        serializer = PersonSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonDetail(APIView):
    """
    Retrieve, update or delete a person instance.
    """

    def get_object(self, pk):
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = PersonSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = PersonSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
