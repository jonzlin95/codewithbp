from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Community(models.Model):
    name = models.CharField(max_length=32)
    users = models.ManyToManyField(User)

    def get_num_users(self):
        return CustomUser.objects.filter(community=self.id).count()

    def load_articles(self):
        articles = []