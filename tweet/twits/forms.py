from .models import Twit, Comment
from django import forms

class TwitForm(forms.ModelForm):
    class Meta:
        model=Twit
        fields=('body', 'image')

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('body',)
