from django.db import models
from codewithbp.apps.article.models import Article
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    favorites = models.ManyToManyField(Article)
