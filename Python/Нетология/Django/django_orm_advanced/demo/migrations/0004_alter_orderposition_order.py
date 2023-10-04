# Generated by Django 4.2.5 on 2023-10-04 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_remove_order_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderposition',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='demo.order'),
        ),
    ]
