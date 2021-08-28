from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,related_name='student')


    def __str__(self):
    	return self.user.username





class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,related_name='teacher')
    phone=models.CharField(max_length=200)
    course=models.CharField(max_length=200)


    def __str__(self):
    	return self.user.username


class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='user_profile')
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)
    description=models.TextField(blank=True)
    full_name=models.CharField(max_length=264,blank=True)
    dob=models.DateField(blank=True,null=True)