from django.urls import path,re_path

from post.views import index ,category ,tag,postDetail,contact,contactSuccess,send_email

from django.urls import register_converter

urlpatterns = [
    #path('/',index, name ='index'),
    path('',index,name='index'),
    path('post/',index, name='index'),
  	path('contact/', contact, name='contact'),
   	path('contact/success/', contactSuccess, name='contactsuccess'), 
    path('category/<slug:category_url>',category, name='category'),
    re_path(r'^tags/(?P<slug>[-\w]+)/$',tag, name='tags'),
    re_path(r'^(?P<slug>[-\w]+)/$', postDetail, name='postdetail'),
    path('send_email',send_email,name='send_email'),
    
   
    #path('tags/<slug:tag_url>',tag, name='tags'),
    #path('<slug:post_url>',postDetail, name='postdetail'),
    #path('<(?P<post_url>[-a-zA-Z0-9_]+)$>',postDetail, name='postdetail'),
]