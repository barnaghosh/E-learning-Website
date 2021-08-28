from django import forms
from django.forms import fields
from question.models import Ans

class AnsForm(forms.ModelForm):
    class Meta:
        model=Ans
        fields=('ans',)