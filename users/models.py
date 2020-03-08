from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Users(models.Model):
    """
    User objects have the following fields
    username
    first_name
    last_name
    email
    password
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
