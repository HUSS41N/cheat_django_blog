from django.shortcuts import get_object_or_404, render
from blog.models import BlogPost,BlogComment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def single_blog_post(request,blogpost_id):
    blogpost = get_object_or_404(BlogPost,pk=blogpost_id)
    blogposts = BlogPost.objects.order_by('-blog_date')
    comments = BlogComment.objects.all().filter(blogpost_connected =blogpost)
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            content = request.POST['content']
            current_user = request.user
            comment = BlogComment(content=content,author=current_user,blogpost_connected=blogpost)
            comment.save()
    
    context = {
        'blogpost':blogpost,
        'blogposts':blogposts,
        'comments':comments
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