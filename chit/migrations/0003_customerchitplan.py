# Generated by Django 4.1.2 on 2024-03-13 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("chit", "0002_monthwisechitdetails"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomerChitPlan",
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
                (
                    "customer_chit_details",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="chit.chitdetails",
                    ),
                ),
                (
                    "customer_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
