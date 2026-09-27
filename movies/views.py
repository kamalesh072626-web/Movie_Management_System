from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MovieForm
from .models import Movie


def movie_list(request):
    movies = Movie.objects.all().order_by('-created_at')

    search_query = request.GET.get('search', '').strip()
    genre = request.GET.get('genre', '')
    watched = request.GET.get('watched', '')

    if search_query:
        movies = movies.filter(
            Q(title__icontains=search_query) |
            Q(director__icontains=search_query)
        )

    if genre:
        movies = movies.filter(genre=genre)

    if watched == 'watched':
        movies = movies.filter(watched=True)
    elif watched == 'unwatched':
        movies = movies.filter(watched=False)

    context = {
        'movies': movies,
        'genres': Movie.GENRE_CHOICES,
        'search_query': search_query,
        'selected_genre': genre,
        'selected_watched': watched,
    }

    return render(request, 'movies/movie_list.html', context)


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    return render(
        request,
        'movies/movie_detail.html',
        {'movie': movie}
    )


def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)

        if form.is_valid():
            movie = form.save()

            messages.success(
                request,
                f'"{movie.title}" was added successfully.'
            )

            return redirect('movie_list')

    else:
        form = MovieForm()

    return render(
        request,
        'movies/movie_form.html',
        {
            'form': form,
            'page_title': 'Add Movie'
        }
    )


def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)

        if form.is_valid():
            movie = form.save()

            messages.success(
                request,
                f'"{movie.title}" was updated successfully.'
            )

            return redirect('movie_detail', pk=movie.pk)

    else:
        form = MovieForm(instance=movie)

    return render(
        request,
        'movies/movie_form.html',
        {
            'form': form,
            'page_title': 'Edit Movie'
        }
    )


def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == 'POST':
        title = movie.title
        movie.delete()

        messages.success(
            request,
            f'"{title}" was deleted successfully.'
        )

        return redirect('movie_list')

    return render(
        request,
        'movies/movie_confirm_delete.html',
        {'movie': movie}
    )