from django.db import models
from django.urls import reverse


class Person(models.Model):
    name = models.CharField(max_length=128)

    # def get_absolute_url(self):
    #     return reverse("coreapp:person-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through="Membership")

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
