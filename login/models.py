from django.db import models

# Create your models here.

class loginModel(models.Model):
    user = models.CharField(max_length=20)
    pasw = models.CharField(max_length=30, blank=True, null=True)

def __str__(self):
    return 
