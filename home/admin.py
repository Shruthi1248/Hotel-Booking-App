from django.contrib import admin

from home.views import logout

# Register your models here.
from .models import *

admin.site.register(Amenities)
admin.site.register(Hotel)
admin.site.register(HotelImages)
admin.site.register(HotelBooking)
admin.site.register(offers)
