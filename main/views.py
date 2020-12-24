from django.shortcuts import render
from blog.models import BlogPost,Blogger,Category

def index(request):
    blogposts = BlogPost.objects.order_by('-blog_date')
    featured_blogposts = BlogPost.objects.order_by('-blog_date')
    categories = Category.objects.all()
    context = {
        'blogposts':blogposts,
        'featured_blogposts':featured_blogposts,
        'categories':categories
    }
    return render(request,'main/index.html',context)

def about(request):
    return render(request,'main/about.html')

def search(request):
    query = request.GET['query']
    queryset_title = BlogPost.objects.order_by('-blog_date').filter(title__icontains=query)
    context = {
        'blogposts':queryset_title,
    }

    return render(request,'main/search.html',context)