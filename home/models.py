from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Medicine(models.Model):
    medicine_name= models.CharField(max_length=100)
    number_of_tablets = models.IntegerField()
    expiry_date = models.DateField()
