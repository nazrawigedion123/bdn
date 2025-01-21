from django import forms
from .models import Vacancy

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'description', 'location', 'company', 'salary', 'job_type', 'application_deadline']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'title'}),
            'description': forms.Textarea(attrs={'rows': 4,'class':'form-control'}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
            'company':forms.TextInput(attrs={'class':'form-control'}),
            'salary':forms.TextInput(attrs={'class':'form-control'}),
          

            'application_deadline': forms.SelectDateWidget(attrs={'class':'form-control',}),
        }