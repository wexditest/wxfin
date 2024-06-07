# Generated by Django 4.1.2 on 2024-05-31 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chit", "0009_alter_customerchitpaymentdetails_chit_month_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customerchitplan",
            name="category",
            field=models.CharField(
                blank=True,
                choices=[("Customer", "Customer"), ("Management", "Management")],
                default="Customer",
                max_length=100,
            ),
        ),
    ]