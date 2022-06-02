from django import forms
from django.forms import ModelForm
from .models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['content']
        



class CommentForm(ModelForm):
    class Meta:
        model = Comments 
        fields = ['body']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        self.fields['body'].widget.attrs.update({'rows': '4'})