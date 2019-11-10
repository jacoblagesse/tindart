from django import forms
from django.forms import ModelForm, Textarea
from tindartapp.models import User, Artist, Art
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
'''
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'firstname', 'lastname')
        widgets = {
            'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
'''
class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = ('username', 'firstname', 'lastname')
        widgets = {
            'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

class ArtForm(ModelForm):
    class Meta:
        model = Art
        fields = ('artwork',)
        widgets = {
            'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )