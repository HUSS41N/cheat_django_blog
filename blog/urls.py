from django.urls import path
from . import views

urlpatterns = [
    path('blogpost',views.single_blog_post,name='single_blog_post')
]