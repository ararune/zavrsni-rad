# Generated by Django 5.0.6 on 2024-05-17 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0039_kategorija_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kategorija',
            name='slug',
        ),
    ]
