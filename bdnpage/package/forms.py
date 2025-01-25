from django import forms
from django.core.validators import FileExtensionValidator

from .models import Package, Feature, Order, Custom, Category


class SVGAndImageFormField:
    pass


class CategoryForm(forms.ModelForm):
    class Meta():
        model = Category
        fields = ['name',  'image','description']
        image = forms.FileField(

            validators=[FileExtensionValidator(['svg'])]
        )
        
        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control  textinputclass', 'placeholder': 'name'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control editable medium-editor-textarea textinputclass',
                       'placeholder': 'description'}),

        }


class PackageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PackageForm, self).__init__(*args, **kwargs)

        # Fetch all categories
        categories = Category.objects.prefetch_related("feature_set").all()

        # Create choices grouped by category
        choices = []
        for category in categories:
            features = category.feature_set.all()
            if features:
                choices.append((category.name, [(feature.id, feature.name) for feature in features]))

        # Features that have no category
        uncategorized_features = Feature.objects.filter(category__isnull=True)
        if uncategorized_features.exists():
            choices.append(("Uncategorized", [(feature.id, feature.name) for feature in uncategorized_features]))

        # Create the checkbox select multiple field
        self.fields["features"] = forms.MultipleChoiceField(
            choices=choices,
            widget=forms.CheckboxSelectMultiple(),
            required=False,
        )
    class Meta():
        model = Package
        fields = ['name', 'description', 'image', 'features','most_pop']
        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control  textinputclass', 'placeholder': 'name'}),
            'features': forms.SelectMultiple(attrs={'class': 'form-control  textinputclass', 'placeholder': 'feature'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control editable medium-editor-textarea textinputclass',
                       'placeholder': 'description'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'most_pop':forms.CheckboxInput()
        }


class FeatureForm(forms.ModelForm):
    class Meta():
        model = Feature
        fields = ['name', 'description','category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'description'}),
            'category':forms.Select(attrs={'class': 'form-control',})
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