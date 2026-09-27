from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'director',
        'genre',
        'language',
        'release_year',
        'rating',
        'watched',
    )

    list_filter = (
        'genre',
        'language',
        'watched',
    )

    search_fields = (
        'title',
        'director',
    )