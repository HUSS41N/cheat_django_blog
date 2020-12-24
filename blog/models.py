from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.fields import TextField
from ckeditor.fields import RichTextField
class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title 

class Blogger(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    blogger = models.ForeignKey(Blogger,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=50)
    content = RichTextField(blank=True,null=True)
    # content = models.TextField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    blog_date = models.DateTimeField(default=datetime.now,blank=True)
    
    def __str__(self):
        return self.title

    @property
    def number_of_comments(self):
        return BlogComment.objects.filter(blogpost_connected=self).count()

class BlogComment(models.Model):
    blogpost_connected = models.ForeignKey(BlogPost,related_name='comments',on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.author) + ', ' + self.blogpost_connected.title[:40]