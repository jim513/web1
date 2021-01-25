from django.urls import path
from user.views import profile,login,signup ,changepassword,changepasswordsuccess
from django.contrib.auth import views as authViews 

urlpatterns = [
   	
    path('profile/',profile,name='profile'),
    path('signup/',signup,name='signup'),
   	path('login/', authViews.LoginView.as_view(template_name='login.html'), name='login'),
   	path('logout/', authViews.LogoutView.as_view(), {'next_page' : 'index'}, name='logout'),
    path('changepassword/',changepassword,name='change_password'),
    path('changepassword/success',changepasswordsuccess,name='change_password_success'),

   	path('passwordreset/', authViews.PasswordResetView.as_view(), name='password_reset'),
   	path('passwordreset/done', authViews.PasswordResetDoneView.as_view(), name='password_reset_done'),
   	path('passwordreset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
   	path('passwordreset/complete/', authViews.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


]