from django.db import models

# Create your models here.
class Members (models.Model) : 
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
