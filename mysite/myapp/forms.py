from django import forms
from myapp import models


class StudentForm(forms.Form):
    class meta:
        model = models.students
        fields = "__all__"