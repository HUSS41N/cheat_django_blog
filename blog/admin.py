from django.contrib import admin

from blog.models import Blogger,BlogPost,Category,BlogComment

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','blogger')
    list_display_links = ('id','title')
    list_filter = ('blogger',)
    list_editable = ('is_published',)
    list_per_page = 20

class BloggerAdmin(admin.ModelAdmin):
    list_display = ('id','name','email')
    list_display_links = ('id','name')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')

class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('id','content')
    list_display_links = ('id',)
    
admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(Blogger,BloggerAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(BlogComment,BlogCommentAdmin)