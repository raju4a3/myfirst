from django.db import models

# Create your models here.
class empdata(models.Model):
	firstname=models.CharField(max_length=10)
	lastname=models.CharField(max_length=10)
	address=models.CharField(max_length=100)

def __str__(self):
	return self.firstname