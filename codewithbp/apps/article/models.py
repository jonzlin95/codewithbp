from datetime import datetime
from django.db import models
from codewithbp.apps.community.models import Community
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    author = models.ForeignKey(User, related_name='author')
    community = models.ForeignKey(Community)
    title = models.CharField(max_length=128)
    link = models.CharField(max_length=128)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    submission_date = models.DateField(default=datetime.now())
    favorited_by = models.ManyToManyField(User)

    def upvote(self):
        self.upvotes += 1

    def downvote(self):
        self.downvotes -= 1

    def get_score(self):
        return self.upvotes - self.downvotes  # todo: something with date

    def get_favorites(self):
        return User.objects.filter(favorited_by__id=self.id)