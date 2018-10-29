from django.conf import settings
from django.db import models
from django.urls import reverse

from rest_framework.reverse import reverse as api_reverse

from phonenumber_field.modelfields import PhoneNumberField


from datetime import date

class CabDriver(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    birth_date = models.DateField(default=date.today)
    driving_license_number = models.CharField(max_length=20, unique=True)
    expiry_date = models.DateField()
    status = models.BooleanField(default=True)
    contact_number = PhoneNumberField()
    rating = models.FloatField()
    email=models.EmailField()
    deaf=models.BooleanField(default=False)
    total_rides=models.IntegerField()

class Cab(models.Model):#for now we are considering that cab driver is the owner of cab.
    license_plate=models.CharField(max_length=15)
    manufacture_year=models.IntegerField()
    status=models.BooleanField(default=False)
    # driver will only be associated only when cab status is active
    driver=models.ForeignKey(CabDriver, on_delete=models.CASCADE, null=True)
    type=models.CharField(max_length=15)
    colour=models.CharField(max_length=20)

class Shift(models.Model):
    driver=models.ForeignKey(CabDriver, on_delete=models.CASCADE)
    cab=models.ForeignKey(Cab, on_delete=models.CASCADE)
    shift_start_time=models.DateTimeField()
    shift_end_time=models.DateTimeField(null=True)
    ongoing=models.BooleanField(default=True)
    rides_completed=models.IntegerField(default=0)