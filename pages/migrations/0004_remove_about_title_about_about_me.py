# Generated by Django 5.0.1 on 2024-01-24 04:48

import ckeditor.fields
import django.utils.timezone
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0003_about"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="about",
            name="title",
        ),
        migrations.AddField(
            model_name="about",
            name="about_me",
            field=ckeditor.fields.RichTextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
