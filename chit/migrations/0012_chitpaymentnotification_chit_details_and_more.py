# Generated by Django 4.1.2 on 2024-06-05 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("chit", "0011_chitpaymentnotification"),
    ]

    operations = [
        migrations.AddField(
            model_name="chitpaymentnotification",
            name="chit_details",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="chit.chitdetails",
            ),
        ),
        migrations.AddField(
            model_name="chitpaymentnotification",
            name="chit_month",
            field=models.CharField(blank=True, max_length=9),
        ),
        migrations.AddField(
            model_name="chitpaymentnotification",
            name="chit_year",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
