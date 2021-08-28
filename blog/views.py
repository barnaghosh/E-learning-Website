from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from blog.models import Blog,Comment,Likes
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,View,DetailView,DeleteView,UpdateView,ListView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse,reverse_lazy
import uuid
from blog.forms import CommentForm


# Create your views here.
def blog_list(request):
    return render(request,'App_Blog/blog_list.html',context={})

class Create_blog(LoginRequiredMixin,CreateView):
    model=Blog
    
    template_name='App_Blog/create_blog.html'
    fields=('blog_title','blog_content','blog_image',)
    def form_valid(self, form):
        block_obj=form.save(commit=False)
        block_obj.author=self.request.user
        title=block_obj.blog_title
        block_obj.slug=title.replace('','-') + '-' +str(uuid.uuid4())
        block_obj.save()
        return HttpResponseRedirect(reverse('app_blog:blog_list'))

class BlogList(LoginRequiredMixin,ListView):
    context_object_name='Blogs'
    model=Blog
    template_name='App_Blog/blog_list.html'
    queryset=Blog.objects.order_by('-publish_date')

@login_required
def details_comment(request,slug):
    blog=Blog.objects.get(slug=slug)
    already_liked=Likes.objects.filter(blog=blog,user=request.user)
    if already_liked:
        liked=True
    else:
        liked=False
    comment_form=CommentForm()
    if request.method=='POST':
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            comment.user= request.user
            comment.blog= blog
            comment.save()
            return HttpResponseRedirect(reverse('app_blog:details',kwargs={'slug':slug}))
    return render(request,'App_Blog/blog_details.html',context={'blog':blog,'comment_form':comment_form,'liked':liked})

@login_required
def liked_page(request,pk):
    blog=Blog.objects.get(pk=pk)
    user=request.user
    already_liked=Likes.objects.filter(blog=blog,user=user)
    if not already_liked:
        like=Likes(blog=blog,user=user)
        like.save()
    return HttpResponseRedirect(reverse('app_blog:details',kwargs={'slug':blog.slug}))


@login_required
def unliked_page(request,pk):
    blog=Blog.objects.get(pk=pk)
    user=request.user
    already_liked=Likes.objects.filter(blog=blog,user=user)
    if already_liked:
        already_liked.delete()
    return HttpResponseRedirect(reverse('app_blog:details',kwargs={'slug':blog.slug}))
    
class MyBlog(LoginRequiredMixin,TemplateView):
    template_name='App_Blog/my_blog.html'

class UpdateBlog(LoginRequiredMixin,UpdateView):
    model=Blog
    fields=('blog_title','blog_content','blog_image',)
    template_name='App_Blog/edit_blog.html'
    def get_success_url(self, **kwargs) :
        return reverse_lazy('app_blog:details',kwargs={'slug':self.object.slug})