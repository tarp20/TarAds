from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Movie




class MovieList(ListView):
    model = Movie

class DetailMovie(DetailView):
    model = Movie
    

# Create your views here.
