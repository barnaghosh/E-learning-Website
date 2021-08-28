from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.

class Ques(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='student_question')
    ques_title=models.CharField(max_length=264,verbose_name='Enter question title')
    slug=models.SlugField(max_length=264)
    url=models.URLField(blank=True)
    ques_content=models.TextField(verbose_name='What is on your mind?')
    ques_image=models.ImageField(upload_to='ques_images',blank=True)
    publish_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['-update_date']
    def __str__(self):
        return self.ques_title

class Ans(models.Model):
    ques=models.ForeignKey(Ques,on_delete=models.CASCADE,related_name='ques_name')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_answer')
    ans=models.TextField(verbose_name='Enter answer')
    ans_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.ans
    class Meta:
        ordering=['-ans_date']