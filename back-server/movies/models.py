from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    id = models.IntegerField(primary_key=True) # 장르 id
    name = models.CharField(max_length=50) # 장르 name

class Movie(models.Model):
    # null, blank : 빈 값, null 가능 여부
    id = models.IntegerField(primary_key=True) # 영화 id
    title = models.CharField(max_length=100)
    release_date = models.DateField(null=True, blank=True)
    popularity = models.FloatField(null=True, blank=True) # 관객 수
    overview = models.TextField(null=True, blank=True)
    vote_average = models.FloatField(null=True, blank=True) # 평점
    vote_count = models.IntegerField(null=True, blank=True) # 평점 투표수
    poster_path = models.CharField(max_length=200, null=True, blank=True)
    # 예고편 링크
    video_url = models.CharField(max_length=200, null=True, blank=True)
    # 장르
    genre_check = models.ManyToManyField(Genre, related_name='genre_movies')
    # 영화를 좋아요한 사용자
    like_movie_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)