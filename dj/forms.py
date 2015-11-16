from django import forms
from django.utils import timezone

class NameForm(forms.Form):
    #error_css_class = 'field-has-error'
    #required_css_class = 'required'

    your_name = forms.CharField(
        label = 'Your name', 
        min_length = 2,
        max_length = 100,
        widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Ann Smith'}),
        error_messages = {'required': 'Please enter your name'}
    )
    your_name.widget_type = 'TextInput'

    date_field = forms.DateField(
        label = 'Enter date', 
        initial = timezone.now(),
        input_formats = ['%Y-%m-%d'],      # e.g., 2006-10-25   - for cleaning and validation
        widget = forms.DateInput(attrs = {'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}, format='%Y-%m-%d'),   # format - for an initial value
        error_messages = {'invalid': 'Please use the following date format: YYYY-MM-DD, e.g. 2017-10-25'}
    )
    date_field.widget_type = 'DateInput'
