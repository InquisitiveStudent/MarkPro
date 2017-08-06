from django import forms
from django.contrib.auth.models import User
from .models import Collection, Newsboard, Bookmarks


class CollectionForm(forms.ModelForm):
    class Meta:
        model=Collection
        fields=['list_title', 'list_type', 'list_description']

class BookmarkForm(forms.ModelForm):
    class Meta:
        model= Bookmarks
        fields= ['bookmarks_title', 'bookmarks_links', 'bookmarks_description']

class NewsboardForm(forms.ModelForm):
    class Meta:
        model= Newsboard
        fields= '__all__'


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model= User
        fields = ['username', 'password', 'email']


