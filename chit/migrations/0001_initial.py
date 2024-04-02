# Generated by Django 4.1.2 on 2024-03-13 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ChitDetails",
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
                ("chit_name", models.CharField(max_length=255)),
                ("chit_total_amt", models.CharField(max_length=255)),
                ("chit_taken_amt", models.CharField(max_length=255)),
                ("chit_nottaken_amt", models.CharField(max_length=255)),
                (
                    "chit_isactive",
                    models.BooleanField(default=False, verbose_name="Chit Status"),
                ),
                (
                    "chit_total_month_count",
                    models.CharField(blank=True, max_length=255),
                ),
                ("chit_start_from", models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
