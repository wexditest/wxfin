# Generated by Django 4.1.2 on 2024-07-07 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("chit", "0014_agentlist_monthwisechitdetails_agent_pay_for_chit_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="monthwisechitdetails",
            name="agent_name",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="chit.agentlist",
            ),
        ),
    ]
