from django import forms
class ClearFeedback(forms.ModelForm):
    date = forms.DateField()
