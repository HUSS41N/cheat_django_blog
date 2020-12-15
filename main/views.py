from django.shortcuts import render
from blog.models import BlogPost,Blogger,Category
# Create your views here.
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