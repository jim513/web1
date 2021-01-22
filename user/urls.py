from django.urls import path
from user.views import profile,login,signup
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('profile/',profile,name='profile'),
    path('signup/',signup,name='signup'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',LoginView.as_view(),{'next_page': 'index'},name='logout'),

]