from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.
class Blog(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_block')
    blog_title=models.CharField(max_length=264,verbose_name='Enter article title')
    slug=models.SlugField(max_length=264)
    blog_content=models.TextField(verbose_name='What is on your mind?')
    blog_image=models.ImageField(upload_to='blog_images',blank=True,verbose_name='article_image')
    publish_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_title


class Comment(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='blog_comment')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comment')
    comment=models.TextField(verbose_name='Enter comment')
    comment_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment

class Likes(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='liked_blog')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='liked_user')