# Generated by Django 5.0.1 on 2024-02-04 20:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0035_alter_client_client_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="education",
            name="website",
            field=models.URLField(blank=True, null=True),
        ),
    ]