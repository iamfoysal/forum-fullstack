from django import forms
from froala_editor.widgets import FroalaEditor
from .models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['content']
        


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['comments']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         for name, field in self.fields.items():
#             field.widget.attrs.update({'class': 'form-control'})
#         self.fields['body'].widget.attrs.update({'rows': '4'})