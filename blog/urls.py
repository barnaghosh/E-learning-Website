from django.urls import path
from blog import views

app_name='app_blog'

urlpatterns = [
    path('',views.BlogList.as_view(),name='blog_list'),
    path('create_blog/',views.Create_blog.as_view(),name='create_blog'),
    path('article_details/<str:slug>/',views.details_comment,name='details'),
    path('liked/<pk>/',views.liked_page,name='liked'),
    path('unliked/<pk>/',views.unliked_page,name='unliked'),
    path('user_article/',views.MyBlog.as_view(),name='user_blog'),
    path('edit_article/<pk>/',views.UpdateBlog.as_view(),name='edit_blog')

]
