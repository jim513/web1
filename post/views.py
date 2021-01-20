from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from post.models import Post

# Create your views here.

def index(request):
    #articles = Post.objects.all()
    articles = Post.objects.filter(status='published').order_by('-created_date')
    template = loader.get_template('index.html')

    context = {
        'articles':articles,
    } 
    return HttpResponse(template.render(context,request))
