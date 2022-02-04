from django.db import models


class City(models.Model):
    """Выбор города для поиска"""
    name = models.CharField('City', max_length=64, blank=False, null=False, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class District(models.Model):
    """Район города"""
    name = models.CharField(max_length=64, )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'


class LocationOwner(models.Model):
    """Владелец локации"""


# class LocationCard(models.Model):
#     rating =

class Location(models.Model):
    """Модель с данными локации"""
    name = models.CharField(max_length=64, )
    district = models.ForeignKey(District, on_delete=models.SET_DEFAULT, default='None')
    address = models.CharField(max_length=64)
    start_work_time = models.TimeField(verbose_name='Start time')
    end_work_time = models.TimeField(verbose_name='End time')

    price = models.PositiveIntegerField(default=0)

    telephone = models.CharField(max_length=20, blank=True)

    google_maps_url = models.URLField()
    site_url = models.URLField(blank=True, null=True)

    description = models.TextField(blank=True, )
    main_image = models.ImageField(blank=True, null=True, upload_to="media/images/locations")

    services = models.ManyToManyField('LocationService', )

    optional_services = models.ManyToManyField('OptionalService', )

    slug = models.SlugField()

    checked = models.BooleanField(default=False, editable=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'


class LocationImages(models.Model):
    """Галерея изображений локации"""
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    image = models.ImageField(verbose_name="Photo", upload_to="media/images/location_photos")
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Location photo'
        verbose_name_plural = 'Location photos'


class LocationService(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    description = models.CharField(max_length=256)
    distributors = models.ManyToManyField('Location', )
    slug = models.SlugField(unique=True)


class OptionalService(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    location = models.ManyToManyField(Location, )


class Review(models.Model):
    email = models.EmailField(verbose_name='Email', blank=False)
    username = models.CharField(verbose_name='Username', max_length=64, blank=False)
    text = models.TextField(verbose_name='Review', max_length=500)
    comment_review = models.ForeignKey('Review', on_delete=models.CASCADE)


class RatingStar(models.Model):
    value = models.FloatField(null=True, default=0)


class Rating(models.Model):
    ip = models.GenericIPAddressField(verbose_name='IP', )
    stars = models.ForeignKey(RatingStar, null=True, default=0, on_delete=models.SET_DEFAULT)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, )

# class RatingGoogle(models.Model):
#
# class  ReviewGoogle(models.Model):
