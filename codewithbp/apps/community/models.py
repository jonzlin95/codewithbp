from django.db import models
from codewithbp.apps.article.models import Article
from django.contrib.auth.models import CustomUser

from article import models.Article

# Create your models here.


class Community(models.Model):

    name = models.CharField(max_length=32)
    users = models.ManyToManyField(CustomUser)

    def get_num_users(self):
        return CustomUser.objects.filter(community=self.id).count()

    def load_articles(self):
        self
