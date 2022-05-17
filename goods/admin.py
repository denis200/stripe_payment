from django.contrib import admin

from goods.models import Currency, Item, Order

admin.site.register(Item)
admin.site.register(Currency)
admin.site.register(Order)