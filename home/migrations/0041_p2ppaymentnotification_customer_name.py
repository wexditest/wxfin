# Generated by Django 4.1.2 on 2024-10-03 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0040_remove_p2ppaymentnotification_p2prequest_obj_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="p2ppaymentnotification",
            name="customer_name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
