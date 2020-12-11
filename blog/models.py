from django.db import models
from datetime import datetime

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
    content = models.TextField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    blog_date = models.DateTimeField(default=datetime.now,blank=True)
    
    def __str__(self):
        return self.title