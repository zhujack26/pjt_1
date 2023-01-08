from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class ArticleListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Article
        # fields = ('id', 'title', 'content')
        fields = ('id', 'title', 'content', 'user', 'username', 'created_at')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)


class ArticleSerializer(serializers.ModelSerializer):
    
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', )

# 게시글 좋아요 등록 및 해제
class ArticleLikeSerializer(serializers.ModelSerializer):


    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username',)
    
    # 좋아요한 작성자
    like_article_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        # 게시글 id, 좋아요한 사용자 목록
        fields = ('id', 'like_article_users', )



