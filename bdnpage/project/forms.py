from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta():
        model = Project
        fields = ['title', 'description', 'image', 'link','date']
        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control  textinputclass', 'placeholder': 'Title'}),
            'link': forms.TextInput(attrs={'class': 'form-control  textinputclass', 'placeholder': 'Link'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control editable medium-editor-textarea textinputclass', 'placeholder': 'Description'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'date': forms.DateTimeInput(attrs={
                'class': 'form-control datetimeinput',
                'placeholder': 'Select Date and Time',
                'type': 'datetime-local'
            }),

        }