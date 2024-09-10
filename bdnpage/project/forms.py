from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta():
        model = Project
        fields = ['title', 'description', 'image', 'link']
        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control  textinputclass', 'placeholder': 'Author'}),
            'link': forms.TextInput(attrs={'class': 'form-control  textinputclass', 'placeholder': 'Author'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control editable medium-editor-textarea textinputclass', 'placeholder': 'Quote'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }