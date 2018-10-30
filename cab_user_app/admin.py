from django.contrib import admin

from .models import CabUser, CabRide, CabRideStatus

# Register your models here.
admin.site.register(CabRide)
admin.site.register(CabUser)
admin.site.register(CabRideStatus)