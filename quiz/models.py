from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.
class Course(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='course_name')
    course_name = models.CharField(max_length=50,verbose_name='Quiz title',)
    # question_number = models.PositiveIntegerField(null=True)
    publish_date=models.DateTimeField(auto_now_add=True,null=True)
    class Meta:
        ordering=['-publish_date']
    def __str__(self):
        return self.course_name

class Question(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='question',verbose_name='Quiz title')
    marks=models.PositiveIntegerField(null=True)
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)

class Result(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE,related_name='student_result')
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)