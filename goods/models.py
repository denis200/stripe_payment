from django.db import models
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save
import environ
import stripe

env = environ.Env(DEBUG=(bool, False))
stripe.api_key = env('SKSTRIPE')


class Currency(models.Model):
    """ Модель валюты """
    currency = models.CharField(verbose_name=_('Currency'),max_length=3)

    def __str__(self):
        return self.currency


class Item(models.Model):
    """ Модель товара """
    name = models.CharField(verbose_name=_('Name'), max_length=100)
    description = models.CharField(verbose_name=_('Description'), max_length=250)
    price = models.DecimalField(verbose_name=_('Price'),max_digits=10, decimal_places=2,default=0)
    currency = models.ForeignKey(Currency,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Order(models.Model):
    """ Модель заказа """
    total_price = models.DecimalField(verbose_name=_('Price'),max_digits=10, decimal_places=2,default=0)
    items = models.ManyToManyField(Item,related_name='items')


@receiver(post_save, sender=Item)
def save_user(sender, instance,created ,**kwargs):
    """ При создании товара создается продукт и его цена 
    """
    if created:
        product = stripe.Product.create(name=instance.name,description = instance.description)
        stripe.Price.create(
            unit_amount=int(str(instance.price).replace('.','')),
            currency=instance.currency,
            product=product.id,
        )






