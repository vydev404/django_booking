from django.db import models


# Create your models here.

class City(models.Model):
    name = models.CharField(verbose_name='City name', max_length="64", blank=False, null=False, unique=True)
    slug = models.SlugField(unique=True)


class District(models.Model):
    name = models.CharField(verbose_name='District name', max_length="128", blank=False, null=False)
    city_location = models.ForeignKey(City, verbose_name='District of city', on_delete=models.CASCADE)
    slug = models.SlugField()


class LocationImages(models.Model):
    image_name = models.CharField()
    image_path = models.FilePathField()
    image_size = models.PositiveIntegerField()
    image_hash = models.CharField()


class LocationOwner(models.Model):
    username = models.CharField(max_length='24', verbose_name='Owner username', null=False)
    first_name = models.CharField(max_length='24', verbose_name='Owner 1st name', null=False)
    second_name = models.CharField(max_length='24', verbose_name='Owner 2nd name', null=False)

    organization = models.CharField(max_length='24', verbose_name='Organization name', null=False)

    email = models.EmailField()


# class LocationCard(models.Model):
#     rating =

class Location(models.Model):
    district = models.ForeignKey(District, verbose_name='District of location', on_delete=models.CASCADE)
    title = models.CharField(max_length="256", verbose_name='Location name')
    slug = models.SlugField()
    description = models.TextField(verbose_name='Location description', null=True)
    image_main = models.ImageField()
    image_pool = models.ForeignKey(LocationImages, null=True, blank=True)

    location_owner = models.ForeignKey(LocationOwner, on_delete=models.CASCADE)

    google_coordinates = models.CharField()
