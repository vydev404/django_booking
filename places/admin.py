from django.contrib import admin

# Register your models here.
from .models import City, District, Location, LocationImages


class LocationAdmin(admin.ModelAdmin):

    search_fields = ['district', 'title', 'address']
    ordering = ['title', 'district', 'owner']


admin.site.register(City)
admin.site.register(District)
admin.site.register(LocationImages)
admin.site.register(Location, LocationAdmin)
