# Generated by Django 4.1.2 on 2024-10-03 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0032_p2pcreditemi_payment_choice_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="p2pcreditemi",
            name="payment_month",
            field=models.CharField(
                choices=[
                    (1, "January"),
                    (2, "Feburary"),
                    (3, "March"),
                    (4, "April"),
                    (5, "May"),
                    (6, "June"),
                    (7, "July"),
                    (8, "August"),
                    (9, "September"),
                    (10, "October"),
                    (11, "November"),
                    (12, "December"),
                ],
                default=10,
                max_length=9,
            ),
        ),
    ]
