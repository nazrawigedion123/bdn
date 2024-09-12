from django import forms
from .models import Package, Feature, Order, Custom


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



# class CustomForm(forms.ModelForm):
#     feature = forms.ModelMultipleChoiceField(
#         queryset=Feature.objects.all(),
#         widget=forms.CheckboxSelectMultiple,  # For checkboxes, or RadioSelect for radio buttons
#         required=True
#     )
#
#     class Meta:
#         model = Custom
#         fields = ['feature']
#
class CustomForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Group features by package
        packages = Package.objects.prefetch_related('features').all()
        for package in packages:
            features = package.features.all()
            self.fields[f'package_{package.id}'] = forms.ModelMultipleChoiceField(
                queryset=features,
                widget=forms.CheckboxSelectMultiple,  # Checkboxes for multiple selection
                required=False,
                label=package.name
            )

    class Meta:
        model = Custom
        fields = []