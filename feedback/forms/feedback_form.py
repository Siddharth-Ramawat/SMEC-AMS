from django import forms

from ..models import Feedback
INFRASTRCUTURE = 'INF'
GENERIC = 'GEN'
CURRICULUM = 'CUR'

FEEDBACK_CHOICES = (
        (INFRASTRCUTURE,'Infrastructure'),
        (GENERIC,'Generic'),
        (CURRICULUM,'Curriculum'),
    )

class FeedbackForm(forms.ModelForm):
    username = forms.CharField(max_length=120)
    class Meta:
         model = Feedback
         include = ['username']
         exclude = ['user']

        