from django.http.response import HttpResponseRedirect
from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from quiz.forms import QuestionForm,CourseForm,QuestionFormAnother
from quiz.models import Question,Course
from App_Login.models import Teacher
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required,user_passes_test
# Create your views here.

# class CreateQuiz(CreateView):
#     fields=('course_name','question_number',)
#     model=Course
#     template_name='quiz/create.html'
#     def get_success_url(self):
#         print('pk')
#         print(self.get_object)
def is_teacher(user):
    try:
        return user.is_authenticated and user.teacher is not None
    except Teacher.DoesNotExist:
        return False
@user_passes_test(is_teacher)
def create_quiz(request,pk):
    course=Course.objects.get(pk=pk)
    form=QuestionFormAnother()
    if 'save' in request.POST:
        form=QuestionFormAnother(request.POST)
        # print(form)
        if form.is_valid():
            form=form.save(commit=False)
            form.course=course
            form.save()
            return HttpResponseRedirect(reverse('quiz:quiz_shit'))
    if 'another' in request.POST:
        form=QuestionFormAnother(request.POST)
        # print(form)
        if form.is_valid():
            form=form.save(commit=False)
            form.course=course
            form.save()
            return HttpResponseRedirect(reverse('quiz:create_question',kwargs={'pk':pk}))
    return render(request,'quiz/create_ans.html',context={'form':form})

@user_passes_test(is_teacher)
def create_course(request):
    form=CourseForm()
    if request.method == 'POST':
        form=CourseForm(request.POST)
        # print(form.pk)
        if form.is_valid():
            form=form.save(commit=False)
            form.author=request.user
            form.save()
            pk=form.pk
            print(form.pk)
            return HttpResponseRedirect(reverse('quiz:create_question',kwargs={'pk':pk}))
    return render(request,'quiz/create.html',context={'form':form})

@login_required
def quiz_paper(request):
    course=Course.objects.all()
    if request.method =='POST':
        print(request)
    return render(request,'quiz/quiz_shit.html',context={'course':course})

@user_passes_test(is_teacher)
def create_another_quiz(request):
    
    form=QuestionForm()
    if 'save' in request.POST:
        form=QuestionForm(request.POST)
        # print(form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('quiz:quiz_shit'))
    if 'another' in request.POST:
        form=QuestionForm(request.POST)
        # print(form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('quiz:create'))
    return render(request,'quiz/create_ans.html',context={'form':form})

