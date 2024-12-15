from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=60, verbose_name='model name')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='price')
    image = models.URLField(max_length=200, verbose_name='image')
    release_date = models.DateField(verbose_name='release date')
    lte_exists = models.BooleanField(verbose_name='LTE on board')
    slug = models.SlugField(max_length=200, unique=True)

