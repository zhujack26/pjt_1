from datetime import date
from django.http import JsonResponse
from django.db.models import Count
from django.shortcuts import get_object_or_404
from .models import *
from .serializers.movie import *
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

movies = Movie.objects.annotate(
like_movie_users_count = Count('like_movie_users', distinct=True),) # 좋아요한 사용자 수

# Create your views here.

# 전체 영화 조회(메인)
# 인증 안해도 조회만 가능
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly]) # 인증된 사용자는 모든 요청 가능, 인증되지 않은 사용자는 GET만 가능
def movies_main(request):
    # 인기 높은 순서로 정렬, 관객 수 높은 순으로 정렬
    # 정렬기준에 따라 쿼리문 수정하여 정렬 가능!!
    main_movies = movies.filter(release_date__lte=date.today()).order_by('-release_date','-vote_average')[:10]
    serializer = MovieListSerializer(main_movies, many=True)
    print(main_movies)
    return Response(serializer.data)

# 필터링된 영화 정보
@api_view(['GET'])
# @permission_classes([IsAuthenticatedOrReadOnly]) # 인증된 사용자는 모든 요청 가능, 인증되지 않은 사용자는 GET만 가능
def movie_sort(request, sort_num):
    if sort_num == 1: # 관객수(popularity)
        sort_movies = movies.order_by('-popularity')[:30]
    elif sort_num == 2: # 최신순(개봉한 영화만)
        sort_movies = movies.filter(release_date__lte=date.today()).order_by('-release_date')[:10]
    elif sort_num == 3: # 개봉예정작 : 빠른 개봉 순으로
        sort_movies = movies.filter(release_date__gt=date.today()).order_by('release_date')[:10]
    elif sort_num == 4: # 리뷰 많은 순(개봉한 영화만), 최신순
        sort_movies = movies.filter(release_date__lte=date.today()).order_by('-review_movie_count', '-release_date')[:10]
    elif sort_num == 5: # 평점순(vote_average/개봉한 영화)
        sort_movies = movies.filter(release_date__lte=date.today()).order_by('-vote_average') [:10]
    # 장르 포함
    elif sort_num == 12: # 모험
        sort_movies = movies.filter(genre_check=12).order_by('-vote_average', 'release_date')[:10]
    elif sort_num == 14: # 판타지
        sort_movies = movies.filter(genre_check=14).order_by('-vote_average', 'release_date')[:10]
    elif sort_num == 16: # 애니메이션
        sort_movies = movies.filter(genre_check=16).order_by('-vote_average', 'release_date')[:10]
    elif sort_num == 18: # 드라마
        sort_movies = movies.filter(genre_check=18).order_by('-vote_average', 'release_date')[:10]
    elif sort_num == 27: # 공포
        sort_movies = movies.filter(genre_check=27).order_by('-vote_average', 'release_date')[:10]
    elif sort_num == 28: # 액션
        sort_movies = movies.filter(genre_check=28).order_by('-vote_average', 'release_date')[:10]
    elif sort_num == 35: # 코미디
        sort_movies = movies.filter(genre_check=35).order_by('-vote_average', 'release_date')[:10]
    elif sort_num == 36: # 역사
        sort_movies = movies.filter(genre_check=36).order_by('-vote_average', 'release_date')[:10]
    elif sort_num == 37: # 서부
        sort_movies = movies.filter(genre_check=37).order_by('-vote_average', 'release_date')[:10]
    elif sort_num == 53: # 스릴러
        sort_movies = movies.filter(genre_check=53).order_by('-vote_average', 'release_date')[:10]
    elif sort_num == 80: # 범죄
        sort_movies = movies.filter(genre_check=80).order_by('-vote_average', 'release_date')[:10]
    elif sort_num == 99: #다큐멘터리
        sort_movies = movies.filter(genre_check=99).order_by('-vote_average', 'release_date')[:10]
    elif sort_num == 878: # SF
        sort_movies = movies.filter(genre_check=878).order_by('-vote_average', 'release_date')[:10]
    elif sort_num == 9648: # 미스터리
        sort_movies = movies.filter(genre_check=9648).order_by('-vote_average', 'release_date')[:10]
    elif sort_num == 10402: # 음악
        sort_movies = movies.filter(genre_check=10402).order_by('-vote_average', 'release_date')[:10]
    elif sort_num == 10749: # 로맨스
        sort_movies = movies.filter(genre_check=10749).order_by('-vote_average', 'release_date')[:10]
    elif sort_num == 10751: # 가족
        sort_movies = movies.filter(genre_check=10751).order_by('-vote_average', 'release_date')[:10]
    elif sort_num == 10752: # 전쟁
        sort_movies = movies.filter(genre_check=10752).order_by('-vote_average', 'release_date')[:10]
    elif sort_num == 10770: # TV 영화
        sort_movies = movies.filter(genre_check=10770).order_by('-vote_average', 'release_date')[:10]
    serializer = MovieListSerializer(sort_movies, many=True)
    return Response(serializer.data)

# 단일 영화 조회
# 인증안해도 조회만 가능
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly]) # 인증된 사용자는 모든 요청 가능, 인증되지 않은 사용자는 GET만 가능
def movie_detail(request, movie_pk):
    movie = movies.get(pk=movie_pk)
    serializer = MovieListSerializer(movie)
    return Response(serializer.data)

# 영화 좋아요 등록 및 해제(좋아요 수까지 출력)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated]) # 인증된 사용자만 권한 허용

def movie_like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    # 해제
    if movie.like_movie_users.filter(pk=user.pk).exists():
        movie.like_movie_users.remove(user)
    # 등록
    else:
        movie.like_movie_users.add(user)

    serializer = MovieLikeSerialzer(movie)

    like_movie_register = {
        'id' : serializer.data.get('id'),
        'like_movie_users_count' : movie.like_movie_users.count(),
        'like_movie_users' : serializer.data.get('like_movie_users'),
    }
    return JsonResponse(like_movie_register)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_exist(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    ans = 0
    if movie.like_movie_users.filter(pk=user.pk).exists():
        ans = 1
    else:
        ans = 0
    return Response(ans)
        
        

# # 영화가 DB에 존재하면 좋아요 실행, 없으면 영화를 DB에 담고 좋아요 실행
# def movie_like(request, movie_pk):
#     TMDB_API_KEY = '38ee27fa3688e2ed93068da12e4c2386'

#     movie = get_object_or_404(Movie, pk=movie_pk)
#     user = request.user
#     # pk 가 movie_pk에 값이 있다면 존재하고
#     if movie.objects.filter(pk=movie_pk).exists():

#         # movie = get_object_or_404(Movie, pk=movie_pk)
#         # user = request.user

#         # 해제
#         if movie.like_movie_users.filter(pk=user.pk).exists():
#             movie.like_movie_users.remove(user)
#         # 등록
#         else:
#             movie.like_movie_users.add(user)

#         serializer = MovieLikeSerialzer(movie)

#         like_movie_register = {
#             'id' : serializer.data.get('id'),
#             'like_movie_users_count' : movie.like_movie_users.count(),
#             'like_movie_users' : serializer.data.get('like_movie_users'),
#         }
#     else:
#         add_data= []

#         for i in range(1, 2):
#             request_url = f'https://api.themoviedb.org/3/movie/{movie['id']}?api_key={TMDB_API_KEY}&language=ko-KR&page={i}'
#             movie = request.get(request_url).json()

#             fields = {
#                     'title': movie['title'],
#                     'release_date': movie['release_date'],
#                     'popularity': movie['popularity'],
#                     'overview': movie['overview'],
#                     'vote_average': movie['vote_average'],
#                     'vote_count' : movie['vote_count'],
#                     'poster_path': movie['poster_path'],
#                     'video_url': [],
#                     'genre_check': movie['genre_ids'],
#                     'like_movie_users' : [],
#                 }

#             data = {
#                 "model": "movies.movie",
#                 "pk": movie['id'],
#                 "fields": fields
#             }

#             add_data.append(data)

#             serializer = MovieListSerializer(data=data)
#             if serializer.is_valid():
#                 serializer.save()
        
#             movie = get_object_or_404(Movie, pk=movie_pk)        
#             user = request.user
#             # 해제
#             if movie.like_movie_users.filter(pk=user.pk).exists():
#                 movie.like_movie_users.remove(user)
#             # 등록
#             else:
#                 movie.like_movie_users.add(user)

#             serializer = MovieLikeSerialzer(movie)

#             like_movie_register = {
#                 'id' : serializer.data.get('id'),
#                 'like_movie_users_count' : movie.like_movie_users.count(),
#                 'like_movie_users' : serializer.data.get('like_movie_users'),
#             }

#     return JsonResponse(like_movie_register)