from django.shortcuts import render
from django.http import HttpResponse

from .models import students
from myapp import forms
# Create your views here.
def home(request):
    students_list = students.objects.order_by('Name')
    diction = {'students' : students_list}
    return render(request, 'myapp/index.html', context=diction)


def form(request):
    new_form = forms.StudentForm('Name')
    diction = {'test_form' : new_form}
    return render(request, 'myapp/form.html', context=diction)