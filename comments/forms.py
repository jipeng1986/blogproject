"""
作者    ：Jimingpeng
创建时间：2018/9/3  16:33 
"""

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']
