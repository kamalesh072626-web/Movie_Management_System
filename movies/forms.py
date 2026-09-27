from django import forms
from django.core.exceptions import ValidationError
from datetime import date

from .models import Movie


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = [
            'title',
            'director',
            'genre',
            'language',
            'release_year',
            'rating',
            'duration',
            'watched',
            'description',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter movie title'
            }),

            'director': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter director name'
            }),

            'genre': forms.Select(attrs={
                'class': 'form-control'
            }),

            'language': forms.Select(attrs={
                'class': 'form-control'
            }),

            'release_year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Example: 2024'
            }),

            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0 - 10',
                'step': '0.1'
            }),

            'duration': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Duration in minutes'
            }),

            'watched': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter movie description',
                'rows': 4
            }),
        }

    def clean_release_year(self):
        year = self.cleaned_data['release_year']

        if year > date.today().year:
            raise ValidationError(
                "Release year cannot be in the future."
            )

        if year < 1888:
            raise ValidationError(
                "Please enter a valid movie release year."
            )

        return year

    def clean_title(self):
        title = self.cleaned_data['title'].strip()

        if len(title) < 2:
            raise ValidationError(
                "Movie title must contain at least 2 characters."
            )

        return title

    def clean_duration(self):
        duration = self.cleaned_data['duration']

        if duration <= 0:
            raise ValidationError(
                "Movie duration must be greater than 0 minutes."
            )

        return duration