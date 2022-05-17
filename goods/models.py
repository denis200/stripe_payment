from django.db import models
from django.utils.translation import gettext_lazy as _


class Item(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=100)
    description = models.CharField(verbose_name=_('Description'), max_length=250)
    price = models.DecimalField(verbose_name=_('Price'),max_digits=10, decimal_places=2,default=0)