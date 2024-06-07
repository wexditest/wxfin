# Generated by Django 4.1.2 on 2024-05-23 13:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0017_incomeexpenses_entry_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="LotterySpinList",
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
                ("title", models.CharField(blank=True, max_length=255, null=True)),
                ("option1", models.CharField(blank=True, max_length=255, null=True)),
                ("option2", models.CharField(blank=True, max_length=255, null=True)),
                ("option3", models.CharField(blank=True, max_length=255, null=True)),
                ("option4", models.CharField(blank=True, max_length=255, null=True)),
                ("option5", models.CharField(blank=True, max_length=255, null=True)),
                ("option6", models.CharField(blank=True, max_length=255, null=True)),
                ("option7", models.CharField(blank=True, max_length=255, null=True)),
                ("option8", models.CharField(blank=True, max_length=255, null=True)),
                ("entry_date", models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]