from decimal import Decimal
import decimal
import random
from django.db import transaction
from django.core.management.base import BaseCommand
from mixer.backend.django import mixer
from goods.models import Currency,Item


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Currency,Item]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        names = ['Картофель','Молоко','Лук','Огурцы','Помидоры']
        desc = ['вкусный','обыкновенный','ядреный','зеленые','свежие']

        currencys = mixer.cycle(2).blend('goods.Currency',currency = 'rub')

        mixer.cycle(5).blend('goods.Item',
                                name = mixer.sequence(*names),
                                description = mixer.sequence(*desc),
                                currency = mixer.sequence(*currencys),
                                price = mixer.sequence(*[decimal.Decimal(random.randrange(1155, 32389))/100 for i in range(5)])
                            )