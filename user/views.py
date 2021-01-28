from django.shortcuts import render ,redirect,get_object_or_404
from user.forms import SignupForm ,ChangePasswordform,EditProfileForm
from django.contrib.auth.models import User ,Permission
from post.views import index
from post.models import Category

from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

from user.models import Profile
from django.template import loader
from django.http import HttpResponse
from django.core.paginator import Paginator

# Create your views here.
def profile(request,username):
    #검색
    query = request.GET.get("q")
    if query:
        return index(request)

    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    articles = profile.favorites.all()
    
    #Pagination
    paginator = Paginator(articles, 6)
    page_number = request.GET.get('page')
    articles_paginator = paginator.get_page(page_number)
    
    categories = Category.objects.all()

    template = loader.get_template('profile.html')
    context = {
        'articles': articles_paginator,
        'profile':profile,
        'categories':categories,
        }
        
    return HttpResponse(template.render(context, request))

def login(request):
    return render(request,'login.html')

def signup(request):
    #검색
    query = request.GET.get("q")
    if query:
        return index(request)
       
    if request.method =='POST':
        
        form = SignupForm(request.POST)
        
        if(form.is_valid()):
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            u =User.objects.create_user(username=username,email=email,password=password,is_staff=True)
            permission = Permission.objects.get(name='Can add post')
            u.user_permissions.add(permission)
            permission = Permission.objects.get(name='Can change post')
            u.user_permissions.add(permission)
            permission = Permission.objects.get(name='Can view post')
            u.user_permissions.add(permission)
            permission = Permission.objects.get(name='Can add category')
            u.user_permissions.add(permission)
            permission = Permission.objects.get(name='Can change category')
            u.user_permissions.add(permission)
            permission = Permission.objects.get(name='Can add tag')
            u.user_permissions.add(permission)
            permission = Permission.objects.get(name='Can change tag')
            u.user_permissions.add(permission)
            return redirect('index')
        
    else:
        form = SignupForm()
    
    categories = Category.objects.all()

    context ={
        'form' :form,
        'categories':categories,
    }

    return render(request,'signup.html',context)

@login_required
def changepassword(request):
    #검색
    query = request.GET.get("q")
    if query:
        return index(request)

    user =request.user
    if request.method =="POST":
        form =ChangePasswordform(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request,user)
            return redirect('change_password_success')
    else:
        form= ChangePasswordform(instance=user)

    categories = Category.objects.all()


    context ={
        'form' :form,
        'categories':categories,
    }

    return render(request,'change_password.html',context)

def changepasswordsuccess(request):
    return render(request,'change_password_success.html')


@login_required
def editprofile(request):
    #검색
    query = request.GET.get("q")
    if query:
        return index(request)

    user =request.user.id
    profile = Profile.objects.get(user__id=user)

    if request.method =="POST":
        form =EditProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile.picture = form.cleaned_data.get('picture')
            profile.name = form.cleaned_data.get('name')
            profile.url = form.cleaned_data.get('url')
            profile.profile_info = form.cleaned_data.get('profile_info')
            profile.save();
            return redirect('index')
    else:
        form= EditProfileForm()

    categories = Category.objects.all()


    context ={
        'form' :form,
        'categories':categories,
    }

    return render(request,'editprofile.html',context)

