from django import forms
from .models import Package, Feature, Order


class PackageForm(forms.ModelForm):
    class Meta():
        model = Package
        fields = ['name', 'description', 'image', 'features']
        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control  textinputclass', 'placeholder': 'name'}),
            'features': forms.SelectMultiple(attrs={'class': 'form-control  textinputclass', 'placeholder': 'feature'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control editable medium-editor-textarea textinputclass',
                       'placeholder': 'description'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }


class FeatureForm(forms.ModelForm):
    class Meta():
        model = Feature
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'description'})
        }

class OrderForm(forms.ModelForm):
    class Meta():
        model= Order
        fields = ['name','company','phone','email']
        widgets ={
            'name':  forms.TextInput(attrs={'class' :'form-control', 'placeholder':'Name'}),
            'company':  forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Company name'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone no', 'type':'phone'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'email','type':'email'})
        }
