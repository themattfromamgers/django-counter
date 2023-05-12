from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'index.html', context)