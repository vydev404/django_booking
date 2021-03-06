from django.db import models
from services.pricing import get_average_price
from services.gmaps_utils import get_location_coordinates


class District(models.Model):
    """Район города"""
    district_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=64, )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'


class Location(models.Model):
    """Модель с данными локации"""
    name = models.CharField(max_length=64, )
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=64)

    average_price = models.PositiveIntegerField(default=get_average_price)

    coordinates = models.CharField(max_length=128, default=get_location_coordinates)
    google_maps_url = models.URLField(blank=True, null=True)
    site_url = models.URLField(blank=True, null=True)

    description = models.TextField(blank=True, )
    main_image = models.ImageField(blank=True, null=True, upload_to="media/images/locations")
    slug = models.SlugField()

    checked = models.BooleanField(default=False, editable=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class RestingPlaceOwner(models.Model):
    """Владелец места отдыха"""
    # Контактная информация
    name = models.CharField(max_length=64, )
    email = models.EmailField(blank=True, )
    telephone = models.CharField(max_length=20, unique=True)
    # Нужно будет для странички Владельца на сайте
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владельцы'


class LocationRestingPlace(models.Model):
    """Место отдыха """
    title = models.CharField(max_length=64, )  # Краткое название

    description = models.TextField(blank=True, )  # Описание места
    images = models.ImageField(blank=True, null=True, upload_to="media/images/resting_places")

    services = models.ManyToManyField('LocationService', )
    start_work_time = models.TimeField(verbose_name='Start time', default='NULL')
    end_work_time = models.TimeField(verbose_name='End time', default='NULL')
    slug = models.SlugField()

    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(RestingPlaceOwner, on_delete=models.SET_NULL, null=True, blank=True)
    google_maps_url = models.URLField(blank=True, null=True)
    site_url = models.URLField(blank=True, null=True)
    # Status
    checked = models.BooleanField(default=False, editable=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место отдыха'
        verbose_name_plural = 'Места отдыха'


class LocationImages(models.Model):
    """Галерея изображений локации"""
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    image = models.ImageField(verbose_name="Photo", upload_to="media/images/location_photos")
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class LocationService(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    description = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class OptionalService(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дополнительная услуга'
        verbose_name_plural = 'Дополнительные услуги'


class Review(models.Model):
    email = models.EmailField(verbose_name='Email', blank=False)
    username = models.CharField(verbose_name='Username', max_length=64, blank=False)
    text = models.TextField(verbose_name='Review', max_length=500)
    location_review = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    answer_on_review = models.ForeignKey('Review', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Отзыв о {self.location_review.name} от {self.username}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class RatingStar(models.Model):
    STARS_CHOICES = [
        ('0', ''),
        ('1', '*'),
        ('2', '* *'),
        ('3', '* * *'),
        ('4', '* * * *'),
        ('5', '* * * * *'),
    ]
    value = models.CharField(max_length=20, choices=STARS_CHOICES, default='0')

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Звезды'
        verbose_name_plural = 'Звезды'


class Rating(models.Model):
    ip = models.GenericIPAddressField(verbose_name='IP', )
    stars = models.ForeignKey(RatingStar, null=True, default='', on_delete=models.SET_DEFAULT)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, )

    def __str__(self):
        return self.location.name

    class Meta:
        verbose_name = 'Рейтинг'

# class RatingGoogle(models.Model):
#
# class  ReviewGoogle(models.Model):

# class City(models.Model):
#     """Выбор города для поиска"""
#     name = models.CharField('City', max_length=64, blank=False, null=False, unique=True)
#     slug = models.SlugField(unique=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Город'
#         verbose_name_plural = 'Города'
