from django.contrib import admin
from quiz.models import Question,Result,Course
# Register your models here.
admin.site.register(Course)
admin.site.register(Question)
admin.site.register(Result)