# Generated by Django 5.1.6 on 2025-03-18 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_alter_flk_lead_lease_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='flk_lead',
            name='extra',
            field=models.JSONField(default={}),
        ),
    ]
