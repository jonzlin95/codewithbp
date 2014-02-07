from django.shortcuts import render
from codewithbp.apps.customuser.models import CustomUser


# Create your views here.
def get_articles_from_community(request):

    context = {'articles': []}
    for article in Article.objects.filter(community__id=Article.community):
        context['articles'].append(article)
    return render(request, 'template.html', context)
