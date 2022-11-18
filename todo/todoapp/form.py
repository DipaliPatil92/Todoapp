from django import forms
from todoapp.models import Course

class EmpRegister(forms.Form):

    Empname=forms.CharField()
    email=forms.EmailField()
    mobile=forms.CharField()

class CourseForm(forms.ModelForm):
    course_name=forms.CharField()
    course_duration=forms.IntegerField()
    course_category=forms.CharField()
    course_fees=forms.FloatField()

    class Meta:
        model=Course
        #fields="__all__"
        fields=["course_name","course_duration","course_category","course_fees"]


        