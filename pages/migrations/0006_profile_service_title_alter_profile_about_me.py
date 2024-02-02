# Generated by Django 5.0.1 on 2024-01-24 12:37

import ckeditor.fields
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0005_profile_about_me"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="service_title",
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="profile",
            name="about_me",
            field=ckeditor.fields.RichTextField(
                default="say something about your self here"
            ),
        ),
    ]