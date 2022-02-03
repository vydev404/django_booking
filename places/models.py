import datetime

from django.db import models
from django.utils import timezone
from datetime import datetime


class City(models.Model):
    "Выбор города для поиска"
    name = models.CharField('City', max_length=64, blank=False, null=False, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class District(models.Model):
    "Район города"
    name = models.CharField('District name', max_length=128, blank=False, null=False)
    city_location = models.ForeignKey(City, verbose_name='District of city', on_delete=models.CASCADE)
    description = models.TextField('District description', default='')
    slug = models.SlugField(max_length=64, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'District'
        verbose_name_plural = 'Districts'


class LocationOwner(models.Model):
    "Владелец локации"
    username = models.CharField(max_length=32, verbose_name='Owner username', null=False)
    first_name = models.CharField(max_length=32, verbose_name='Owner 1st name', null=False)
    second_name = models.CharField(max_length=32, verbose_name='Owner 2nd name', null=False)

    organization = models.CharField(max_length=32, verbose_name='Organization name', null=False)

    email = models.EmailField()

    def __str__(self):
        return '{} {}'.format(self.first_name, self.second_name)


# class LocationCard(models.Model):
#     rating =

class Location(models.Model):
    "Модель с данными локации"

    district = models.ForeignKey(District,
                                 verbose_name='District of location',
                                 on_delete=models.SET_NULL,
                                 null=True
                                 )
    address = models.CharField('Address', max_length=256, null=False)
    title = models.CharField(max_length=256, verbose_name='Location name')
    slug = models.SlugField()
    short_description = models.TextField(max_length=256)
    description = models.TextField(verbose_name='Location description', null=True)
    image_main = models.ImageField('Photo', upload_to='img/locations/')
    #image_pool = models.ManyToOneRel('Album with images', LocationImages)

    creation_time = models.DateTimeField('Created', default=timezone.now)

    owner = models.ForeignKey(LocationOwner, on_delete=models.SET_NULL, null=True)

    location_site_or_maps_link = models.URLField('Site link')
    google_coordinates = models.CharField(max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'


class LocationImages(models.Model):
    "Галерея изображений локации"
    name = models.CharField(verbose_name='Name', max_length=256)
    description = models.TextField(verbose_name='Description', null=True, default='')
    image = models.ImageField('Photo', upload_to='img/locations_gallery/', blank=True)
    location = models.ForeignKey(Location, verbose_name='photo', on_delete=models.CASCADE, null=True)
    size = models.PositiveIntegerField('Size', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Location photo'
        verbose_name_plural = 'Location photos'

