from django.contrib import admin

# Register your models here.
from .models import *


class LocationAdmin(admin.ModelAdmin):
    search_fields = ['district', 'name', 'address']
    ordering = ['name', 'district', ]


admin.site.register(District)
admin.site.register(LocationRestingPlace)
admin.site.register(RestingPlaceOwner)
admin.site.register(Location)
admin.site.register(LocationImages)

admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Review)
admin.site.register(OptionalService)
admin.site.register(LocationService)
