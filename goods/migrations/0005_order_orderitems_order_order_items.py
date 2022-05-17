# Generated by Django 4.0.4 on 2022-05-17 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_currency_item_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Price')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='goods.item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='goods.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='order_items',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='goods.orderitems'),
        ),
    ]
