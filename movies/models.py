from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Movie(models.Model):

    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
        ('Romance', 'Romance'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Thriller', 'Thriller'),
        ('Other', 'Other'),
    ]

    LANGUAGE_CHOICES = [
        ('English', 'English'),
        ('Tamil', 'Tamil'),
        ('Hindi', 'Hindi'),
        ('Telugu', 'Telugu'),
        ('Malayalam', 'Malayalam'),
        ('Kannada', 'Kannada'),
        ('Other', 'Other'),
    ]

    title = models.CharField(max_length=200)

    director = models.CharField(max_length=100)

    genre = models.CharField(
        max_length=20,
        choices=GENRE_CHOICES
    )

    language = models.CharField(
        max_length=20,
        choices=LANGUAGE_CHOICES
    )

    release_year = models.PositiveIntegerField()

    rating = models.FloatField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ]
    )

    duration = models.PositiveIntegerField(
        help_text="Duration in minutes"
    )

    watched = models.BooleanField(default=False)

    description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title