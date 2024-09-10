from django import forms
from .models import Testimonials


class TestimonialsForm(forms.ModelForm):
    class Meta():
        model = Testimonials
        fields = [ 'person', 'position','image','testimonial']
        widgets = {

            'person': forms.TextInput(attrs={'class': 'form-control  textinputclass','placeholder':'Author'}),
            'position': forms.TextInput(attrs={'class': 'form-control  textinputclass','placeholder':'Author'}),
            'testimonial': forms.Textarea(attrs={'class': 'form-control editable medium-editor-textarea textinputclass','placeholder':'Quote'}),

            

        }