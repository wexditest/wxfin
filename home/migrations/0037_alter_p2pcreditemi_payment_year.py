# Generated by Django 4.1.2 on 2024-10-03 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0036_alter_p2pcreditemi_payment_month"),
    ]

    operations = [
        migrations.AlterField(
            model_name="p2pcreditemi",
            name="payment_year",
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
