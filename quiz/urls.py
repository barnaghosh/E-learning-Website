from django.urls import path
from quiz import views

app_name='quiz'

urlpatterns = [
    # path('create_quiz_question/',views.create_another_quiz,name='create'),
    path('create_quiz_question/<int:pk>/',views.create_quiz,name='create_question'),
    path('create_quiz/',views.create_course,name='course'),
    path('quiz/',views.quiz_paper,name='quiz_shit'),
    
]
