from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from .forms import MovieForm
from .forms import MovieFilterForm

def index(request):
    movies = Movie.objects.all()
    form = MovieFilterForm(request.GET or None)

    if form.is_valid():
        genre = form.cleaned_data.get('genre')
        year = form.cleaned_data.get('year')
        if genre:
            movies = movies.filter(genre=genre)
        if year:
            movies = movies.filter(release_year=year)

    return render(request, 'movies/index.html', {'movies': movies, 'form': form})



def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/edit_movie.html', {'form': form, 'movie': movie})

def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MovieForm()
    return render(request, 'movies/add_movie.html', {'form': form})

def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        movie.delete()
        return redirect('index')
    return render(request, 'movies/delete_movie.html', {'movie': movie})