# Generated by Django 4.1.2 on 2024-04-23 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("share", "0007_dividendtrade_dividend_yield_dividendtrade_yield_msg"),
    ]

    operations = [
        migrations.AddField(
            model_name="dividendtrade",
            name="record_date",
            field=models.CharField(default="", max_length=255),
        ),
    ]