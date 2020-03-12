from django.db import models
<<<<<<< HEAD
=======
from django.contrib.auth.models import User

>>>>>>> c2065e07c530b187ea855bada6bccc73f2ce37b1
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