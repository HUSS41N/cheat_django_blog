from django.shortcuts import get_object_or_404, render
from blog.models import BlogPost
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def single_blog_post(request,blogpost_id):
    blogpost = get_object_or_404(BlogPost,pk=blogpost_id)
    context = {
        'blogpost':blogpost
    }
    return render(request,'blog/single_blog.html',context)

def all_blog_post(request):
    blogposts = BlogPost.objects.order_by('-blog_date')
    paginator = Paginator(blogposts,6)
    page = request.GET.get('page')
    paged_blogposts = paginator.get_page(page)
    
    context = {
        'blogposts':paged_blogposts
    }
    return render(request,'blog/blogposts.html',context)