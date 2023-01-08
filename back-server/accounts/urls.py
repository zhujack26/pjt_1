from django.urls import path
from . import views

app_name = 'accounts'
# 회원가입(POST) : account/signup/
# 프로필 정보 조회 및 수정(GET/PUT) : account/user
# 비밀번호 변형(POST) : account/password/change/
# 비밀번호 찾기(POST) : account/password/reset

urlpatterns = [
    path('delete/', views.user_delete), # 회원탈퇴
    path('<int:user_pk>/list/', views.user_movie_list), # 사용자가 좋아요/위시리스트/평점을 준 영화 목록 조회각 목록과 그 수를 출력)
    path('<int:user_pk>/profile/', views.user_profile),# 상대방 프로필 조회
    # path('<int:user_pk>/profile/', views.user_profile),# 상대방 프로필 조회
    # path("kakao/login/callback/", views.kakao_login) # Kakao Login
]