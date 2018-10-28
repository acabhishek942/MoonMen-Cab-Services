from django.conf import settings
from django.db import models
from django.urls import reverse

from rest_framework.reverse import reverse as api_reverse

from phonenumber_field.modelfields import PhoneNumberField


from datetime import date

# django hosts --> subdomain for reverse

class CabUser(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    birth_date = models.DateField(default=date.today)
    status = models.BooleanField(default=True)
    contact_number = PhoneNumberField()
    rating = models.FloatField(min_value=0, max_value=5)