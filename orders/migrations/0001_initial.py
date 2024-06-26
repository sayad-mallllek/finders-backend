# Generated by Django 4.2.13 on 2024-05-18 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('providers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderBasket',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total_price', models.FloatField()),
                ('number_of_items', models.IntegerField()),
                ('items_link', models.CharField(max_length=255)),
                ('items_weight', models.FloatField()),
                ('shipping_charge', models.FloatField()),
                ('shipped_at', models.DateTimeField(blank=True, null=True)),
                ('received_at', models.DateTimeField(blank=True, null=True)),
                ('shipping_provider_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.shippingprovider')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total_price', models.FloatField()),
                ('number_of_items', models.IntegerField()),
                ('items_link', models.CharField(max_length=255)),
                ('delivery_charge', models.FloatField()),
                ('ordered_at', models.DateTimeField(blank=True, null=True)),
                ('delivered_at', models.DateTimeField(blank=True, null=True)),
                ('has_received_price', models.BooleanField(default=False)),
                ('bill_id', models.CharField(max_length=255)),
                ('customer_delivery_charge', models.FloatField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
                ('delivery_provider_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.deliveryprovider')),
                ('order_basket_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.orderbasket')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
