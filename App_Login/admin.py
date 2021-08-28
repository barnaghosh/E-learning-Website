from django.contrib import admin

# Register your models here.
from App_Login.models import User,Student,Teacher,UserProfile


admin.site.register(User)

admin.site.register(Student)

admin.site.register(Teacher)
admin.site.register(UserProfile)