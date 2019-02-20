from django import forms

class TodoForm(forms.Form):
    content = forms.CharField()
    author = forms.CharField()
    date_created = forms.DateTimeField()
    completed = forms.BooleanField()

