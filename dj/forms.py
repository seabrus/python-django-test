from django import forms
from django.utils import timezone

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    date_field = forms.DateField(label='Enter date', initial=timezone.now())

