from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from App_Login.forms import Login_form
from django.views.generic import CreateView,UpdateView
from .forms import StudentSignUpForm,TeacherSignUpForm,EditProfile
from .models import User,Student,UserProfile
from django.contrib.auth.decorators import login_required
from django.urls import reverse,reverse_lazy
from quiz.models import Question
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.



@login_required
def home(request):
    dic={}
    print(request.user.is_student)
    print(request.user.is_teacher)
    return HttpResponseRedirect(reverse('app_blog:blog_list'))


def login_page(request):
    form=Login_form()
    if request.method == 'POST':
        form=Login_form(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('App_Login:home'))
    return render(request,'App_Login/login.html',context={'title':'Login','form':form})

class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'App_Login/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        user_profile=UserProfile(user=user)
        user_profile.save()
        login(self.request, user)
        return redirect('App_Login:home')

class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'App_Login/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        user_profile=UserProfile(user=user)
        user_profile.save()
        login(self.request, user)
        return redirect('App_Login:home')


@login_required
def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:login'))


@login_required
def edit_profile(request):
    print(request.user)
    current_user=UserProfile.objects.get(user=request.user)
    form=EditProfile(instance=current_user)
    if request.method=='POST':
        form=EditProfile(request.POST,request.FILES,instance=current_user)
        if form.is_valid():
            form.save()
            form=EditProfile(instance=current_user)
            # app_login:profile
            return HttpResponseRedirect(reverse('main'))
    return render(request,'App_Login/edit_profile.html',context={'form':form})

# class UpdateBlog(LoginRequiredMixin,UpdateView):
#     model=UserProfile
#     fields=('profile_pic','blog_content','blog_image',)
#     template_name='App_Blog/edit_blog.html'
#     def get_success_url(self, **kwargs) :
#         return reverse_lazy('app_blog:details',kwargs={'slug':self.object.slug})


@login_required
def profile(request):
    return render(request,'App_Login/profile.html',context={})


@login_required
def profile_others(request,username):
    user_other=User.objects.get(username=username)
    if user_other==request.user:
        return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request,'App_Login/profile_others.html',context={'user_other':user_other,})
