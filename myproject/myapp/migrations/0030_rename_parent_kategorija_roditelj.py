# Generated by Django 5.0.6 on 2024-05-15 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_kategorija_oglas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kategorija',
            old_name='parent',
            new_name='roditelj',
        ),
    ]
