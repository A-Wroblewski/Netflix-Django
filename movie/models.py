from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

CATEGORIES_LIST = (
    ('cats', 'Gatos'),
    ('programming', 'Programação'),
    ('is_it_cake', 'É bolino ou bolina?'),
    ('others', 'Outros'),
)


class Movie(models.Model):
    thumbnail = models.ImageField(upload_to='movies_thumbnails')
    title = models.CharField(max_length=80)
    description = models.TextField(max_length=500, blank=True)
    category = models.CharField(max_length=15, choices=CATEGORIES_LIST)
    views = models.IntegerField(default=0)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Episode(models.Model):
    movie = models.ForeignKey('Movie', related_name='episodes', on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    video = models.URLField()

    def __str__(self):
        return f'{self.movie.title} - {self.title}'


class User(AbstractUser):
    watched_movies = models.ManyToManyField('Movie')
