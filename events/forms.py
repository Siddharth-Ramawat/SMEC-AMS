from django import forms
from .models import Events, Poll
import datetime


# date checker
def present_or_future_date(value):
    if value < datetime.date.today():
        raise forms.ValidationError("The date cannot be in the past!")
    return value


class DateInput(forms.DateInput):
    input_type = 'date'


class EventsCreation(forms.ModelForm):
    text = forms.CharField(max_length=400, widget=forms.Textarea())
    event_date = forms.DateField(validators=[present_or_future_date], widget=DateInput)
    venue = forms.CharField(empty_value='')

    class Meta:
        model = Events
        widgets = {'event_date': DateInput()}
        exclude = ['username', 'user']

    def __init__(self, *args, **kwargs):
        super(EventsCreation, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['email'].widget.attrs['readonly'] = True


class Polls(forms.ModelForm):
    class Meta:
        model = Poll
        include = ['event_id']
        exclude = ['username']
