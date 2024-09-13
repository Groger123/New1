"""
URL configuration for hollymovies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from viewer.views import *

urlpatterns = [

    path('movie/update/<pk>/', MovieUpdateView.as_view(), name='movie_update'),
    path('admin/', admin.site.urls, name='admin'),

    path('', home, name='home'),





    #path('movies/', movies, name='movies'),
    #path('movies/', MoviesView.as_view(), name='movies'),
    #path('movies/', MoviesTemplateView.as_view(), name='movies'),
    path('movies/', MoviesListView.as_view(), name='movies'),
    path('movie/<pk>/', movie, name='movie'),

    #path('creators/', creators, name='creators'),
    #path('creators/', CreatorsView.as_view(), name='creators'),
    #path('creators/', CreatorsTemplateView.as_view(), name='creators'),
    path('creators/', CreatorsListView.as_view(), name='creators'),

    path('movie/create/', MovieCreateView.as_view(), name='movie_create'),

    path('movie/delete/<pk>/', MovieDeleteView.as_view(), name='movie_delete'),

    path('creator/create/', CreatorCreateView.as_view(), name='creator_create'),

    path('creator/update/<pk>/', CreatorUpdateView.as_view(), name='creator_update'),
    path('creator/delete/<pk>/', CreatorDeleteView.as_view(), name='creator_delete'),



    #path('movie/update/<pk>/', CreatorUpdateView.as_view(), name='movie_update'),
    #path('movie/delete/<pk>/', CreatorDeleteView.as_view(), name='movie_delete'),





    path('creator/<pk>/', creator, name='creator'),

    path('genre/<pk>/', GenreView.as_view(), name='genre'),




    path('creators/actor/', CreatorsListViewActor.as_view(), name='creator_actor'),
    path('creators/director/', CreatorsListViewDirector.as_view(), name='creator_director'),
    path('creators/all/', CreatorsListView.as_view(), name='creator_all'),





]
