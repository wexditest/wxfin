# Generated by Django 4.1.2 on 2024-07-07 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chit", "0013_chitdetails_chit_isstarted"),
    ]

    operations = [
        migrations.CreateModel(
            name="AgentList",
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
                ("agent_name", models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name="monthwisechitdetails",
            name="agent_pay_for_chit",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="monthwisechitdetails",
            name="disburment_pic",
            field=models.ImageField(default="avatar.jpg", upload_to="disburment_pic/"),
        ),
        migrations.AddField(
            model_name="monthwisechitdetails",
            name="payment_mode",
            field=models.CharField(
                blank=True,
                choices=[("", "--"), ("Online", "Online"), ("Cash", "Cash")],
                default="",
                max_length=9,
            ),
        ),
    ]