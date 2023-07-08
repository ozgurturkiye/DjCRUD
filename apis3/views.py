from django.urls import reverse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from apis3.serializers import PersonSerializer
from coreapp.models import Person


class Home(APIView):
    def get(self, request):
        data = {
            "person-list": request.build_absolute_uri(reverse("apis2:person-list")),
            "person-detail": request.get_full_path() + "{lookup}/",
        }
        return Response(data)


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
