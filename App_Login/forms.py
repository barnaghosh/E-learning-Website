from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.db import transaction

from .models import Student, User,Teacher,UserProfile

class StudentSignUpForm(UserCreationForm):
    email=forms.EmailField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username=forms.CharField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password1=forms.CharField(required=True,label='',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2=forms.CharField(required=True,label='',widget=forms.PasswordInput(attrs={'placeholder':'Password Confirmation'}))

  
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        return user


class TeacherSignUpForm(UserCreationForm):
    email=forms.EmailField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username=forms.CharField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password1=forms.CharField(required=True,label='',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2=forms.CharField(required=True,label='',widget=forms.PasswordInput(attrs={'placeholder':'Password Confirmation'}))
    phone=forms.CharField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':'Enter phone number'}))
    course=forms.CharField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':'course'}))
  
    class Meta(UserCreationForm.Meta):
        model = User
        fields=('email','username','password1','password2','phone','course')
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email=self.cleaned_data.get('email')
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.phone=self.cleaned_data.get('phone')
        teacher.course=self.cleaned_data.get('course')
        teacher.save()

        return user


class Login_form(AuthenticationForm):
    username=forms.CharField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password=forms.CharField(required=True,label='',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    class Meta:
        model=User
        fields=('username','password')

class EditProfile(forms.ModelForm):
    dob=forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model=UserProfile()
        exclude=('user',)