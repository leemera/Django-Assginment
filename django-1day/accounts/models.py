from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager  # 매니저도 직접 만들 것

class CustomUser(AbstractUser):
    # 필요하다면 추가 필드
    objects = CustomUserManager()
