__author__ = 'CRUCIFIX'

from django import forms

class EventForm(forms.Form):
    program = forms.CharField(label='Program', max_length=100)
    spot = forms.CharField(label='Spot', max_length=100)
    start_date = forms.CharField(label='Start_date', max_length=100)
    start_time = forms.CharField(label='Start_time', max_length=100)
    duration = forms.CharField(label='Duration', max_length=100)
    description = forms.CharField(widget=forms.Textarea())
