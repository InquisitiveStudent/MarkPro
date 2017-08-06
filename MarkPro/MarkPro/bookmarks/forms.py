from django import forms
from django.contrib.auth.models import User
from .models import Collection,newsboard, bookmarks


class CollectionForm(forms.Form):
    class Meta:
        model=Collection
        fields=['__all__']

class BookmarkForm(forms.Form):
    class Meta:
        model= bookmarks
        fields=['__all__']

class NewsboardForm(forms.Form):
    class Meta:
        model= newsboard
        fields=['__all__']


class LoginForm(forms.Form):
    class Meta:
        model= User

        password = forms.CharField(widget=forms.PasswordInput)

        fields=['username', 'password', 'email']


