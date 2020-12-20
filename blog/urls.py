from django.urls import path
from . import views

urlpatterns = [
    path('<int:blogpost_id>',views.single_blog_post,name='single_blog_post'),
    path('blogposts',views.all_blog_post,name='all_blog_post')
]