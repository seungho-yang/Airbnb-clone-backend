# Generated by Django 4.1.2 on 2022-12-06 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0002_alter_category_created_at_alter_category_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="category",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
