from django import forms
from django.db.models import fields
from .models import BlogComment

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['content']