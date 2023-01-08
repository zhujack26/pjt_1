import json
import random
import datetime
import pandas as pd
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .serializers.account import *
# from movies.serializers.rate import *
from rest_framework import status
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
# 랜덤 장르 담아오기
# Kakao Login
import os
import requests
from datetime import datetime, timedelta
import jwt

User = get_user_model()

# Create your views here.
# 회원 가입
# 인증 없이 접근 가능한 영역 : 추후 인증 필요
@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = AccountSignUpSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(request)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 프로필 정보 조회 및 수정
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated]) # 인증된 사용자만 권한 허용
def profile_update(request, username):
    Users = get_object_or_404(User, username=username)
    if request.user == User:
        serializer = ProfileSerializer(instance=Users, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            serializer = ProfileSerializer(Users)
            return Response(serializer.data)


# 회원 탈퇴
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_delete(request):
    request.user.delete()
    data = {
        'content': f'{request.user}님의 탈퇴처리가 완료되었습니다.'
    }
    return Response(data, status=status.HTTP_204_NO_CONTENT)

# 사용자가 좋아요 영화 목록 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated]) # 인증된 사용자만 권한 허용
def user_movie_list(request, user_pk):
    Users = get_object_or_404(User, pk=user_pk)
    serializer = UserMovieListSerializer(Users)
    user_list = {
        'id' : serializer.data.get('id'),
        'like_movies_count' : Users.like_movies.count(),
        'like_movies' : serializer.data.get('like_movies'),
    }
    return JsonResponse(user_list)

# 상대방 프로필 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated]) # 인증된 사용자만 권한 허용
def user_profile(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    serializer = UserProfileSerializer(user)
    return Response(serializer.data)

# # Kakao Login
# @api_view(['POST'])
# @permission_classes([AllowAny])
# def kakao_login(request):
#     code = request.data.get('code')

#     url = 'https://kauth.kakao.com/oauth/token'
#     body = {
#         'grant_type': 'authorization_code',
#         'client_id': os.environ.get("CLIENT_ID"),
#         'redicrect_url': os.environ.get("REDIRECT_URL"),
#         'code': code
#     }

#     kakao_response = requests.post(url, data=body).json()

#     access_token = kakao_response.get('access_token')

#     url = 'https://kapi.kakao.com/v2/user/me'
#     headers = {
#         'Authorization': f'Bearer {access_token}',
#     }

#     kakao_response = requests.get(url, headers=headers).json()

#     kakao_id = kakao_response.get('id')

#     if User.objects.filter(kakao_id=kakao_id).exists():
#         user = get_object_or_404(
#             get_user_model(), kakao_id=kakao_id)

#         token = jwt.encode(
#             {
#                 'user_id': user.pk,
#                 'username': user.username,
#                 'exp': datetime.now() + timedelta(days=1),
#                 'email': user.email
#             },
#             os.environ.get("SECRET_KEY"),
#             algorithm='HS256'
#         )

#         return Response(token, status=status.HTTP_200_OK)

#     kakao_nickname = kakao_response.get(
#         'kakao_account').get('profile').get('nickname')

#     User(
#         kakao_id=kakao_id,
#         username=kakao_nickname).save()

#     user = get_object_or_404(
#         get_user_model(), kakao_id=kakao_id)

#     token = jwt.encode(
#         {
#             'user_id': user.pk,
#             'username': user.username,
#             'exp': datetime.now() + timedelta(days=1),
#             'email': user.email
#         },
#         os.environ.get("SECRET_KEY"),
#         algorithm='HS256'
#     )

#     return Response({'token': token}, status=status.HTTP_200_OK)
