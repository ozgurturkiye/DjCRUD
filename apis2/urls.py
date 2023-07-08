# API Class Base 2(Class base views)
from django.urls import path

from . import views

app_name = "apis2"
urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("persons/", views.PersonList.as_view(), name="person-list"),
    path("persons/<int:pk>/", views.PersonDetail.as_view(), name="person-detail"),
]
