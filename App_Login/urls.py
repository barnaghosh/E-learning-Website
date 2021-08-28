from django.urls import path
from App_Login import views
from django.contrib.auth.views import LogoutView
from django.conf import settings

app_name='App_Login'

urlpatterns = [
    path('home/',views.home,name='home'),
    path('student_signup/',views.StudentSignUpView.as_view(),name='student_signup'),
    path('teacher_signup/',views.TeacherSignUpView.as_view(),name='teacher_signup'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('login/',views.login_page,name='login'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('profile/',views.profile,name='profile'),
    path('profile_others/<username>/',views.profile_others,name='profile_others')
]
