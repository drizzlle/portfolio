# Generated by Django 5.0.1 on 2024-02-03 11:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0028_alter_certificate_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="certificate",
            name="content",
            field=models.TextField(),
        ),
    ]
