from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Genre
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import get_user_model

# User = get_user_model()

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=20)

    # # Kakao Login
    # kakao_id = models.PositiveIntegerField(blank=True)

#     class Meta:
#         model = User
#         fields = ('nickname',)

# class User(UserCreationForm):
#     nickname = models.CharField(max_length=20)

#     class Meta(UserCreationForm.Meta):
#         model = get_user_model()
#         fields = UserCreationForm.Meta.fields + ('nickname',)
