# Generated by Django 5.0.1 on 2024-02-03 11:31

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0027_remove_certificate_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="certificate",
            name="content",
            field=ckeditor.fields.RichTextField(
                default="say something about the certificate"
            ),
        ),
    ]
