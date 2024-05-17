from django import forms

from djangoProject.models import Musician, Album


class CreateMusician(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'
        exclude = ['user']


class CreateAlbum(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        exclude = ['user']



