from django.contrib import admin

from .models import CabDriver, Cab, Shift

# Register your models here.

admin.site.register(Cab)
admin.site.register(CabDriver)
admin.site.register(Shift)

