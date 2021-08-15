from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField

# Create your models here.
class DonationForm(models.Model):
    Name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    search_medicine = models.CharField(max_length=50)
    quantity = models.IntegerField()
    expirydate = models.DateField()
    address = models.CharField(max_length=200)
    class Meta:
        db_table="donationform"