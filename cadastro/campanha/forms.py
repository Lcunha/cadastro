from django import forms
from .models import Post, Comment, Eleitor

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

class EleitorForm(forms.ModelForm):

    class Meta:
        model = Eleitor
        fields = ('nome', 'telefone', 'cidade', 'origem',)
