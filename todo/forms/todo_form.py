import datetime

from django import forms

class TodoForm(forms.Form):
    content = forms.CharField(max_length=20)
    author = forms.CharField(max_length=10)
    date_created = forms.DateTimeField()
    completed = forms.BooleanField(required=False,  initial=False, label='Completed')

#    def clean_author(self):
#        cleaned_data = super(TodoForm, self).clean()
#        content = cleaned_data.get('content')
#        author = cleaned_data.get('author', 'Mr.', 'Mrs.', 'Dr.')
#        date_created = cleaned_data.get('date_completed')
#        completed = cleaned_data.get('completed')
#
#        if not content and not author and not date_created and not completed:
#            raise forms.ValidationError('You have to fill in with the right inputs')


#    def clean_author(self):
#        if not (self.cleaned_data.get('author')
#                    .startswith('Mr.', 'Mrs.', 'Dr.')):
#            raise forms.ValidationError("Please Start with either Mr. , Mrs. or Dr. ")
#
#        return self.cleaned_data.get('author')



