from django.shortcuts import render

# Create your views here.

class Community(models.Model):
    name = models.CharField(max_length=25)