from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import success
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView

from logging import getLogger

LOGGER = getLogger()

from viewer.forms import *
from viewer.models import Movie, Creator, Genre


def home(request):
    retard = ["jablko", "Hruška", "Broskev"]
    context = {'retard': retard}
    return render(request, "home.html", context)



def movies(request):
    movies_ = Movie.objects.all()
    context = {'movies': movies_}
    return render(request, "movies.html", context)


# Class-Based View (CBV)
## View class
class MoviesView(View):
    def get(self, request):
        movies_ = Movie.objects.all()
        context = {'movies': movies_}
        return render(request, "movies.html", context)


## TemplateView class
class MoviesTemplateView(TemplateView):
    template_name = "movies.html"
    extra_context = {'movies': Movie.objects.all()}


## ListView class
class MoviesListView(ListView):
    template_name = "movies.html"
    model = Movie
    # pozor: do template se posílají data jako 'object_list'
    # můžeme to přejmenovat:
    context_object_name = 'movies'

    #pokud bych potřeboval jen nějakou podmnožinu dat (filtr), lze předefinovat context data:
    # pokud chci pouze Krimi filmy:
    """def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        crime_genre = Genre.objects.get(name="Krimi")
        crime_movies = Movie.objects.filter(genres=crime_genre)
        context['movies'] = crime_movies
        return context"""

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        genres = Genre.objects.all()
        context['genres'] = genres
        context['movies'] = Movie.objects.all()
        return context


def movie(request, pk):
    if Movie.objects.filter(id=pk).exists():
        movie_ = Movie.objects.get(id=pk)
        context = {'movie': movie_}
        #print(movie_)
        return render(request, "movie.html", context)
    return movies(request)


def creators(request):
    creators_ = Creator.objects.all()
    context = {'creators': creators_}
    return render(request, "creators.html", context)



class CreatorsView(View):
    def get(self, request):
        creators_ = Creator.objects.all()
        context = {'creators': creators_}
        return render(request, "creators.html", context)


class CreatorsTemplateView(TemplateView):
    template_name = "creators.html"
    extra_context = {'creators': Creator.objects.all()}


class CreatorsListView(ListView):
    template_name = "creators.html"
    model = Creator
    context_object_name = 'creators'
    def get(self, request):
        creators = Creator.objects.all()
        allof = []
        for creator in creators:
            allof.append(creator)

        context = {'allof': allof}
        return render(request, "creators.html", context)


class CreatorsListViewActor(ListView):
    def get(self, request):
        creators = Creator.objects.all()
        actors = []
        for creator in creators:
            if creator.acting.exists():
                actors.append(creator)
        context = {"actors": actors}
        return render(request, "creators.html", context)

class CreatorsListViewDirector(ListView):
    def get(self, request):
        creators = Creator.objects.all()
        directors = []
        for creator in creators:
            if creator.directing.exists():
                directors.append(creator)
        context = {'directors': directors}
        return render(request, "creators.html", context)



def creator(request, pk):
    if Creator.objects.filter(id=pk).exists():
        creator_ = Creator.objects.get(id=pk)
        return render(request, "creator.html", {'creator': creator_})
    return redirect('creators')


class GenreView(View):
    def get(self, request, pk):
        genres = Genre.objects.all()
        genre = Genre.objects.get(id=pk)
        movies = Movie.objects.filter(genres__id=pk)
        context = {'genres': genres, 'genre': genre, 'movies': movies}
        return render(request, "movies.html", context)



class CreatorCreateView(LoginRequiredMixin, FormView):
    template_name = 'form.html'
    form_class = CreatorForm
    success.url = reverse_lazy('creators')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Creator.object.create(
            name=cleaned_data['name'],
            surname=cleaned_data['surname'],
            date_of_birth=cleaned_data['date_of_birth'],
            date_of_death=cleaned_data['date_of_death'],
            country_of_birth=cleaned_data['country_of_birth'],
            country_of_death=cleaned_data['country_of_death'],
            biography=cleaned_data['biography'],
        )
        return result

    def form_invalid(self, form):
        LOGGER.warning('User providet invalit data.')
        return super().form_invalid(form)

class CreatorCreateView(LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = CreatorModelForm
    success_url = reverse_lazy('creators')

    def form_invalid(self, form):
        LOGGER.warning('User providet invalit data.')
        return super().form_invalid(form)

class CreatorUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = CreatorModelForm
    success_url = reverse_lazy('creators')
    model = Creator

    def form_invalid(self, form):
        LOGGER.warning('User providet invalit data updating.')
        return super().form_invalid(form)

class CreatorDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'creator_confirm_delete.html'
    model = Creator
    success_url = reverse_lazy('creators')





class MovieCreateView(CreateView):
    template_name = 'form.html'
    form_class = MovieModelForm
    success_url = reverse_lazy('movies')

    def form_invalid(self, form):
        LOGGER.warning('User providet invalit data updating.')
        return super().form_invalid(form)

class MovieUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = MovieModelForm
    success_url = reverse_lazy('movies')
    model = Movie

    def form_invalid(self, form):
        LOGGER.warning('User providet invalit data updating.')
        return super().form_invalid(form)

class MovieDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'movie_confirm_delete.html'
    model = Movie
    success_url = reverse_lazy('movies')





