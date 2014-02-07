from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils import simplejson

from codewithbp.apps.article.models import Article
from codewithbp.apps.community.models import Community

# Create your views here.


def upvote(request):

    json = simplejson.dumps({'result': 'FAIL'})

    try:
        article_id = int(request.GET['article_id'])
    except:
        return HttpResponse(json, mimetype='application/json')

    article = get_object_or_404(Article, id=article_id)
    article.upvote()

    json = simplejson.dumps({'result': 'OK'})

    return json


def downvote(request):

    json = simplejson.dumps({'result': 'FAIL'})

    try:
        article_id = int(request.GET['article_id'])
    except:
        return HttpResponse(json, mimetype='application/json')

    article = get_object_or_404(Article, id=article_id)
    article.downvote()

    json = simplejson.dumps({'result': 'OK'})

    return json


def submit(request):

    try:
        article_title = str(request.GET['article_title'])
        article_link = str(request.GET['article_link'])
        community_id = id(request.GET['article_community'])
    except:
        return HttpResponse(json, mimetype='application/json')

    article_community = get_object_or_404(Community, id=community_id)

    article_author = request.GET['article_author']
    article_link = request.GET['article_link']
    Article(title=article_title, community=article_community)
            link=article_link).save()

