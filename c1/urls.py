from django.urls import path

from . import views

app_name = "c1"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    # path("persons/", views.PersonListView.as_view(), name="person-list"),
    # path("persons/add/", views.PersonCreateView.as_view(), name="person-add"),
    # path("persons/<int:pk>/", views.PersonDetailView.as_view(), name="person-detail"),
    # path("persons/<int:pk>/change/", views.PersonChangeView.as_view(), name="person-change"),
    # path("persons/<int:pk>/delete/", views.PersonDeleteView.as_view(), name="person-delete"),
]
