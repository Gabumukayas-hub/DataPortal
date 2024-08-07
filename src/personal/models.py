from django.db import models

# Create your models here.
class farmermodels(models.Model):
	name=models.CharField(max_length=50)
	age=models.IntegerField()
	city=models.CharField(max_length=50)
	livestock=models.CharField(max_length=50)
	crop=models.CharField(max_length=50)
	profit_or_loss=models.IntegerField()