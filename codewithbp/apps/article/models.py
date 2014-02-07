from datetime import datetime

from django.db import models
from codewithbp.apps.community import Community
from codewithbp.apps.customuser import CustomUser

# Create your models here.


class Article(models.Model):

    author = models.ForeignKey(CustomUser)
    community = models.ForeignKey(Community)
    link = models.CharField(max_length=128)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    submission_date = models.DateField(default=datetime.now())

    def upvote(self):
        self.upvotes += 1

    def downvote(self):
        self.downvotes -= 1

    def get_score(self):
        return self.upvotes - self.downvotes  # todo: something with date
