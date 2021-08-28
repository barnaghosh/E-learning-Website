from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from question.models import Ques,Ans
from question.forms import AnsForm
from App_Login.models import Student
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
import uuid
# Create your views here.
def is_student(user):
    try:
        return user.is_authenticated and user.student is not None
    except Student.DoesNotExist:
        return False
@login_required
def forum_page(request):
    questions=Ques.objects.all()
    return render(request,'forum/main_page.html',context={'questions':questions})

class Ask_Ques(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model=Ques
    
    template_name='forum/create_question.html'
    fields=('ques_title','ques_content','ques_image','url')
    def form_valid(self, form):
        ques_obj=form.save(commit=False)
        ques_obj.author=self.request.user
        title=ques_obj.ques_title
        ques_obj.slug=title.replace('','-') + '-' +str(uuid.uuid4())
        ques_obj.save()
        return HttpResponseRedirect(reverse('forum:forum_main'))
    def test_func(self):
        obj = self.request.user.is_student
        if obj:
            return True
@login_required
def details_ques(request,slug):
    ques=Ques.objects.get(slug=slug)
    # already_liked=Likes.objects.filter(ques=ques,user=request.user)
    # if already_liked:
    #     liked=True
    # else:
    #     liked=False
    ans_form=AnsForm()
    if request.method=='POST':
        ans_form=AnsForm(request.POST)
        if ans_form.is_valid():
            ans=ans_form.save(commit=False)
            ans.user= request.user
            ans.ques= ques
            ans.save()
            return HttpResponseRedirect(reverse('forum:question_details',kwargs={'slug':slug}))
    return render(request,'forum/ques_details.html',context={'ques':ques,'ans_form':ans_form,})

@login_required
def ques_image(request,pk):
    ques=Ques.objects.get(pk=pk)
    return render(request,'forum/ques_img.html',context={'ques':ques,'img':'img'})

@login_required
def ques_url(request,pk):
    ques=Ques.objects.get(pk=pk)
    return render(request,'forum/ques_img.html',context={'ques':ques,'url':'url'})