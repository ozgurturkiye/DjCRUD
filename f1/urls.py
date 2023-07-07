# f1 Function base 1(Bare metal way with lack of security)
from django.urls import path

from . import views

app_name = "f1"
urlpatterns = [
    path("", views.home, name="home"),
    path("persons/", views.person_list, name="person-list"),
    path("persons/add/", views.person_add, name="person-add"),
    path("persons/<int:pk>/", views.person_detail, name="person-detail"),
    path("persons/<int:pk>/change/", views.person_change, name="person-change"),
    path("persons/<int:pk>/delete/", views.person_delete, name="person-delete"),
]
