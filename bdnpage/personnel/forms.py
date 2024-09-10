from django import forms
from .models import Personnel


class PersonnelForm(forms.ModelForm):
    class Meta():
        model = Personnel
        fields = ['name', 'position', 'image', 'location']
        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control  textinputclass', 'placeholder': 'name'}),
            'position': forms.TextInput(attrs={'class': 'form-control  textinputclass', 'placeholder': 'position'}),
            'location': forms.Textarea(
                attrs={'class': 'form-control textinputclass', 'placeholder': 'location'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }