import datetime

from django import forms

class TodoForm(forms.Form):
    content = forms.CharField(max_length=20)
    author = forms.CharField(max_length=10)
    date_created = forms.DateTimeField()
    completed = forms.BooleanField(required=False,  initial=False, label='Completed')




