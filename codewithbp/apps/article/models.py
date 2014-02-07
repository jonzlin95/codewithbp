from django.db import models
from codewithbp.apps.community import Community
from codewithbp.apps.customuser import CustomUser

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey(CustomUser)
    community = models.ForeignKey(Community)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

