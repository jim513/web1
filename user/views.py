from django.shortcuts import render ,redirect
from user.forms import SignupForm
from django.contrib.auth.models import User
from post.views import index
from post.models import Category
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