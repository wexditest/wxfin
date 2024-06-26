# Generated by Django 4.1.2 on 2024-05-23 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0015_oneslide"),
    ]

    operations = [
        migrations.CreateModel(
            name="IncomeExpenses",
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
                ("income", models.FloatField()),
                ("expense", models.FloatField()),
            ],
        ),
    ]
