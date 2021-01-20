from django.urls import path

from post.views import index
from django.views.generic import TemplateView

urlpatterns = [
    #path('',index, name ='index'),
    path('',index,name='index'),
]