# Generated by Django 4.1.2 on 2024-06-03 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0019_upcomingdividends_stock_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="upcomingdividends",
            name="action",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]