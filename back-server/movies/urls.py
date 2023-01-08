from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.movies_main), # 메인 영화 조회
    path('<int:sort_num>/sort/', views.movie_sort), # 필터링된 영화 정보(장르 포함)
    path('<int:movie_pk>/', views.movie_detail), # 단일 영화 조회
    path('<int:movie_pk>/like/', views.movie_like), # 영화 좋아요 등록 및 해제(좋아요 수까지 출력)
    path('<int:movie_pk>/exist/', views.movie_exist) # DB에 저장된 영화가 존재하는지 판별
]   