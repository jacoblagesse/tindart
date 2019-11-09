from django.forms import ModelForm, Textarea
from tindartapp.models import User, Artist, Art

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'firstname', 'lastname')
        widgets = {
            'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

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