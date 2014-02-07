from django.db import models
from django.contrib.auth.models import AbstractUser
from codewithbp.apps.article.models import Article

# Create your models here.

class CustomUser(AbstractUser):
    favorites = models.ManyToManyField(Article)
