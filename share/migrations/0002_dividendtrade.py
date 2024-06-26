# Generated by Django 4.1.2 on 2024-03-26 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("share", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DividendTrade",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stock_name", models.CharField(max_length=255)),
                ("upload_pic", models.ImageField(upload_to="share/")),
                ("ex_date", models.CharField(max_length=255)),
            ],
        ),
    ]
