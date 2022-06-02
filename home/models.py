from django.contrib.auth.models import User
from django.db import models
from froala_editor.fields import FroalaField

from .helpers import *


class Category (models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True)
   
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural= 'Categories'   

class BlogModel(models.Model):
    title = models.CharField(max_length=1000,null=True , blank=True)
    slug = models.SlugField(max_length=1000, unique=True, null=True , blank=True)
    sub_title =models.CharField(max_length=1000, null=True , blank=True)
    content = FroalaField()
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog')
    category = models. ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
        
    # def summary(self):
    #     return self.content[:30]+"...."

    class Meta:
        verbose_name_plural= 'All Blogs' 
    
    def save(self , *args, **kwargs): 
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user)

    class Meta:
            verbose_name_plural= 'Profile Verification' 



class BlogComment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(BlogModel,on_delete=models.CASCADE, null=True, blank="True")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank="True")
    commented_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
