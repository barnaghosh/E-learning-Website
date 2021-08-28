from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def main(request):
    return HttpResponseRedirect(reverse('app_blog:blog_list'))