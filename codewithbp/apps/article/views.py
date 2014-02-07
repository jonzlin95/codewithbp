from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils import simplejson

from article import models

# Create your views here.


def upvote(request):

    json = simplejson.dumps({'result': 'FAIL'})

    try:
        article_id = int(request.GET['article_id'])
    except:
        return HttpResponse(json, mimetype='application/json')

    article = get_object_or_404(models.Article, id=article_id)
    article.upvote()

    json = simplejson.dumps({'result': 'OK'})

    return json


def downvote(request):

    json = simplejson.dumps({'result': 'FAIL'})

    try:
        article_id = int(request.GET['article_id'])
    except:
        return HttpResponse(json, mimetype='application/json')

    article = get_object_or_404(models.Article, id=article_id)
    article.downvote()

    json = simplejson.dumps({'result': 'OK'})

    return json
