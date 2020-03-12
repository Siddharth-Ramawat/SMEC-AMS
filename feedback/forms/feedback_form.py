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
     class Meta:
         model = Feedback
         exclude = []

        