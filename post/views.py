from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse ,HttpResponseRedirect

from django.template import loader
from django.utils import timezone
from post.models import Post ,Category, Tag
from post.forms import ContactForm
from urllib import parse 
import logging

# Create your views here.

def index(request):
    #articles = Post.objects.all()
    articles = Post.objects.filter(status='published').order_by('-created_date')
    template = loader.get_template('index.html')

    categories = Category.objects.all()

    context = {
        'articles':articles,
        'categories':categories,
    } 

    return HttpResponse(template.render(context,request))

def category(request, category_url):
    articles = Post.objects.filter(status='published').order_by('-created_date')
    categories = Category.objects.all()

    if category_url :
        category = get_object_or_404(Category, slug= category_url)
        articles = articles.filter(category=category)

    template = loader.get_template('category.html')

    context = {
        'articles': articles,
        'category' : category,
        'categories':categories,
    }   
    return HttpResponse(template.render(context,request))

def tag(request, slug):
    articles = Post.objects.filter(status='published').order_by('-created_date')
    categories = Category.objects.all()

    if slug :
        tag = get_object_or_404(Tag, slug= parse.unquote(slug))
        articles = articles.filter(tags=tag)

    template = loader.get_template('tags.html')

    context = {
        'tag' :tag,
        'articles': articles,
        'categories':categories,

    }   
    return HttpResponse(template.render(context,request))

def postDetail(request,slug):

    article = get_object_or_404(Post, slug =parse.unquote(slug))
    template = loader.get_template('post_detail.html')
    categories = Category.objects.all()

    context = {
        'article':article,
        'categories':categories,

    }
    
    return HttpResponse(template.render(context,request))


def Contact(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message =form.save(commit=False)
            message.messge_date = timezone.now()
            form.save()
            return HttpResponseRedirect('contactsuccess')
    else:
        form = ContactForm()
    
    context = {
        'form':form,
    }
    return render(request,'contact.html',context)

def ContactSuccess(request):
    return render(request,'contactsuccess.html')