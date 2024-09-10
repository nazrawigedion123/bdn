from django import forms
from .models import Comment, Subscriber
import re


class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ['name', 'email', 'phone', 'comment']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-field full-width', 'placeholder': 'Your Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control form-field full-width', 'placeholder': 'Your Email', 'type': 'email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control form-field full-width', 'placeholder': 'Your Phone'}),
            'comment': forms.Textarea(attrs={'class': 'form-control form-field full-width', 'placeholder': 'Your Comment'}),
        }

        def clean_email(self):
            email = self.cleaned_data.get('email')
            if not email:
                raise forms.ValidationError("Email is required")
            return email

        def clean_phone(self):
            phone = self.cleaned_data.get('phone')
            if not re.match(r'^\+?\d{10,15}$', phone):
                raise forms.ValidationError(
                    "Phone number must be between 10 and 15 digits and can include an optional leading '+'")
            return phone


class SubscriberForm(forms.ModelForm):
    class Meta():
        model = Subscriber
        fields = ['email']

        widgets = {

            'email': forms.TextInput(attrs={'class': 'form-control form-field full-width', 'placeholder': 'subscribe to out newsletter', 'type': 'email'}),

        }


    def __init__(self, *args, **kwargs):
        super(SubscriberForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = ''

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required")
        if Subscriber.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already subscribed.')
        return email