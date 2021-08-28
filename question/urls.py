from django.urls import path
from question import views

app_name='forum'

urlpatterns = [
    path('',views.forum_page,name='forum_main'),
    path('ask_question/',views.Ask_Ques.as_view(),name='ask_question'),
    path('question_details/<slug>/',views.details_ques,name='question_details'),
    path('question_image/<int:pk>/',views.ques_image,name='question_image'),
    path('question_url/<int:pk>/',views.ques_url,name='question_url'),
]
