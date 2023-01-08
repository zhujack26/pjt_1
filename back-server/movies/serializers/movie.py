from rest_framework import serializers
from movies.models import *
from django.contrib.auth import get_user_model

User = get_user_model()

# 전체/단일/장르별 영화 조회
class MovieListSerializer(serializers.ModelSerializer):   

    class GenreSerializer(serializers.ModelSerializer):
 
        class Meta:
            model = Genre
            # 단일 컬럼 출력 시 ,(콤마) 필수(없으면 인식 못함) 
            fields = '__all__'
    
    genre_check = GenreSerializer(many=True)
    like_movie_users_count = serializers.IntegerField() # 좋아요한 사용자 수


    class Meta:
        model = Movie
        # 영화 id, 좋아요한 사용자 수, 제목, 장르(id, name), 개봉일, 관객 수, 평점, 포스터 주소, 개요
        fields = ('id', 'like_movie_users_count', 'title', 'genre_check', 'release_date', 'popularity', 'vote_average', 'poster_path', 'overview')

# 영화 좋아요 등록 및 해제
class MovieLikeSerialzer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username',)

    # 좋아요한 사용자
    like_movie_users = UserSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        # 영화 id, 좋아요를 한 사용자 목록, 좋아요 수
        fields = ('id','like_movie_users', )