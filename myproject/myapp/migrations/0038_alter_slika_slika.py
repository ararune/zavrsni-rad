# Generated by Django 5.0.6 on 2024-05-17 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0037_alter_slika_slika'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slika',
            name='slika',
            field=models.ImageField(upload_to=''),
        ),
    ]