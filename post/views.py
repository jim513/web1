from django.shortcuts import render, get_object_or_404 ,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

from django.template import loader
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q

from post.models import Post ,Category, Tag
from post.forms import ContactForm
from urllib import parse 
import logging

# Create your views here.
    
def index(request):
    #articles = Post.objects.all()
    articles = Post.objects.filter(status='published').order_by('-created_date')
    categories = Category.objects.all()
    
    #검색
    query = request.GET.get("q")
    if query:
        articles = articles.filter(
       	Q(title__icontains=query)|Q(content__icontains=query)
        ).distinct()

    #페이징
    paginator = Paginator(articles,4)
    page_number =request.GET.get('page')
    
    articles_paginator = paginator.get_page(page_number)

    template = loader.get_template('index.html')
    context = {
        'articles':articles_paginator,
        'categories':categories,
    } 

    return HttpResponse(template.render(context,request))

def category(request, category_url):
    articles = Post.objects.filter(status='published').order_by('-created_date')
    categories = Category.objects.all()
    
    #검색
    query = request.GET.get("q")
    if query:
        #return HttpResponseRedirect(reverse('index',query))
        return index(request)
        #return render(request,'index.html')

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

    #검색
    query = request.GET.get("q")
    if query:
        return index(request)

    article = get_object_or_404(Post, slug =parse.unquote(slug))
    template = loader.get_template('post_detail.html')
    categories = Category.objects.all()

    context = {
        'article':article,
        'categories':categories,

    }
    
    return HttpResponse(template.render(context,request))


def contact(request):
    #검색
    query = request.GET.get("q")
    if query:
        return index(request)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.message_date = timezone.now()
            form.save()
            return redirect('contactsuccess')
    else:
        form = ContactForm()
    
    categories = Category.objects.all()
    context = {
        'form':form,
        'categories':categories,

    }
    return render(request,'contact.html',context)

def contactSuccess(request):
    query = request.GET.get("q")
    if query:
        return index(request)
    return render(request,'contactsuccess.html')