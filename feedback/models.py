from django.db import models
# Create your models here.


class Feedback(models.Model):

    user_name = models.CharField(max_length=120)
    category = models.CharField(max_length=120)
    date_added = models.DateField(auto_now_add=True)
    text = models.CharField(max_length=400)
    email= models.EmailField()

    def __str__(self):
        return self.user_name