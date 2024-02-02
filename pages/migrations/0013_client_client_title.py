# Generated by Django 5.0.1 on 2024-01-24 19:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0012_client"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="client_title",
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
