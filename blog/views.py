from django.shortcuts import render

def single_blog_post(request):
    return render(request,'blog/single_blog.html')

def all_blog_post(request):
    return render(request,'blog/blogposts.html')