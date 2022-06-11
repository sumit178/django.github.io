from django.db import models

# Create your models here.
class contact(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    feedback=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.firstname+ self.lastname
