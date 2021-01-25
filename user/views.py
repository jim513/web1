from django.shortcuts import render ,redirect
from user.forms import SignupForm ,ChangePasswordform
from django.contrib.auth.models import User
from post.views import index
from post.models import Category

from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
# Create your views here.
def profile(request):
    return render(request,'profile.html')

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
            User.objects.create_user(username=username,email=email,password=password)
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