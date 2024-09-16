from django.db import models
from django.db.models import *


# Create your models here.
class Genre(Model):
    name = CharField(max_length=20, null=False, blank=False, unique=True)

    class Meta:
        ordering = ['name']

    def __repr__(self):
        return f"Genre(name={self.name})"

    def __str__(self):
        return f"{self.name}"


class Country(Model):
    name = CharField(max_length=64, null=False, blank=False, unique=True)
    code = CharField(max_length=3, null=False, blank=False, unique=True)

    class Meta:
        verbose_name_plural = "Countries"
        ordering = ['name']

    def __repr__(self):
        return f"Country(name={self.name}, code={self.code})"

    def __str__(self):
        return f"{self.name}"

class Creator(Model):
    name = CharField(max_length=32, null=True, blank=True)
    surname = CharField(max_length=32, null=True, blank=True)
    date_of_birth = DateField(null=True, blank=True)
    date_of_death = DateField(null=True, blank=True)
    country_of_birth = ForeignKey(Country, null=True, blank=True, on_delete=SET_NULL, related_name='creators_born')
    country_of_death = ForeignKey(Country, null=True, blank=True, on_delete=SET_NULL, related_name='creators_died')
    biography = TextField(null=True, blank=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)


    class Meta:
        ordering = ['surname', 'name']

    def __repr__(self):
        return f"Creator(name={self.name}, surname={self.surname})"

    def __str__(self):
        return f"{self.name} {self.surname}"

    def death(self):
        if self.date_of_death is None:
            return ("Žije")
        else:
            return self.date_of_death

class Movie(Model):
    title_orig = CharField(max_length=150, null=False, blank=False)  # https://en.wikipedia.org/wiki/Night_of_the_Day_of_the_Dawn_of_the_Son_of_the_Bride_of_the_Return_of_the_Revenge_of_the_Terror_of_the_Attack_of_the_Evil,_Mutant,_Alien,_Flesh_Eating,_Hellbound,_Zombified_Living_Dead
    title_cz = CharField(max_length=150, null=True, blank=True)
    genres = ManyToManyField(Genre, blank=True, related_name='movies')
    countries = ManyToManyField(Country, blank=True, related_name='movies')
    actors = ManyToManyField(Creator, blank=True, related_name='acting')
    directors = ManyToManyField(Creator, blank=True, related_name='directing')
    length = IntegerField(null=True, blank=True)  # min
    released = IntegerField(null=True, blank=True)  # year
    description = TextField(null=True, blank=True)
    rating = FloatField(null=True, blank=True)  # 0-100
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title_orig', 'released']

    def __repr__(self):
        return f"Movie(title_orig={self.title_orig})"

    def __str__(self):
        return f"{self.title_orig} ({self.released})"

    def lenght_format(self):
        hour = self.length // 60
        minute = self.length % 60
        return f"{hour}:{minute} h"

"""    def __repr__(self):
        return f"Movie(Original name={self.title_orig}"

    def __str__(self):
        return f"{self.title_orig}"


class Review(model):
    user
    movie
    review = CharField(max_length=255, null=True, blank=True)
    rating = IntegerField(null=True, blank=True)
"""