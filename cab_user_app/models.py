from django.conf import settings
from django.db import models
from django.urls import reverse

from rest_framework.reverse import reverse as api_reverse

from phonenumber_field.modelfields import PhoneNumberField
from geoposition.fields import GeopositionField


from cab_driver_app.models import CabDriver, Cab, Shift

from datetime import date

class CabUser(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    birth_date = models.DateField(default=date.today)
    status = models.BooleanField(default=True)
    contact_number = PhoneNumberField()
    rating = models.FloatField()
    email=models.EmailField()
    total_rides=models.IntegerField()

class CabRide(models.Model):
    shift=models.ForeignKey(Shift, on_delete=models.CASCADE)
    ride_start_time=models.DateTimeField(null=True)
    ride_end_time=models.DateTimeField(null=True)
    source_address=models.CharField(max_length=100)
    source_position=GeopositionField()
    destination_address=models.CharField(max_length=100)
    destination_position=GeopositionField()
    cancelled=models.BooleanField(default=False)
    price=models.FloatField()
    payment_type_id=models.IntegerField()
    cancellation_reason=models.CharField(max_length=500, null=True)
    user_ride_complaint=models.CharField(max_length=500, null=True)
    driver_ride_complaint=models.CharField(max_length=500, null=True)

class CabRideStatus(models.Model):
    cab_ride=models.ForeignKey(CabRide, on_delete=models.CASCADE)
    status_id=models.IntegerField()
    status_timestamp=models.DateTimeField()
    status_details=models.CharField(max_length=100)

