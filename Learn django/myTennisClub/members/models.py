from django.db import models

# Create your models here.
class Members (models.Model) : 
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    phone = models.IntegerField(null=True) 
    joined_date = models.DateField(null=True) 

    def __str__(self) : 
        return f"{self.firstName} {self.lastName}"
