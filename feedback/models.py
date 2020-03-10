from django.db import models
from django.contrib.auth.models import User

# Create your models here.
INFRASTRCUTURE = 'INF'
GENERIC = 'GEN'
CURRICULUM = 'CUR'

class Feedback(models.Model):

    FEEDBACK_CHOICES = (
        (INFRASTRCUTURE,'Infrastructure'),
        (GENERIC,'Generic'),
        (CURRICULUM,'Curriculum'),
    )


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=3,
                                choices = FEEDBACK_CHOICES,
                                default=GENERIC)
    date_added = models.DateField(auto_now_add=True)
    text = models.CharField(max_length=400)
    email= models.EmailField()

    def __str__(self):
        return self.user_name