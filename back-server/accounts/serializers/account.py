from dataclasses import field
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model
# from community.models import Review
from movies.models import Genre, Movie

User = get_user_model()

# 회원가입 : 재정의 / url, views를 거치지 않고 조회
# 현재 기본 필드 : 이름, 이메일, 패스워드
# 추가 필드 : 닉네임
class AccountSignUpSerializer(RegisterSerializer):

    nickname = serializers.CharField(max_length=20)

    class Meta:
        model = User
        fields = ('nickname',)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname', '')
        return data

# 프로필 정보 조회 및 수정 : 재정의 / url, views를 거치지 않고 조회됨
class ProfileSerializer(UserDetailsSerializer):

    class GerneSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('id', 'name',)
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id',)

    class Meta:
        model = User
        # 이 부분에 정의되는 부분만 수정 가능('followings' : 팔로워)
        fields = ('id', 'username', 'nickname',)

# 사용자가 좋아요/위시리스트/평점을 준 영화 목록 조회
class UserMovieListSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('id', 'title', 'poster_path',)
    

    # 좋아요 한 영화 목록
    like_movies = MovieSerializer(many=True)

    class Meta:
        model = User
        # 사용자 id, 평가한 영화 목록, 좋아요한 영화 목록, 위시리스트에 담은 영화 목록
        fields = ('id', 'like_movies',)


# 상대방 프로필 조회 
class UserProfileSerializer(UserDetailsSerializer):

    class GerneSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('id', 'name',)
            
    hate_genres = GerneSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'nickname',)