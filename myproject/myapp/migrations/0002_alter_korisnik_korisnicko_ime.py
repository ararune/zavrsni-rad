# Generated by Django 5.0.2 on 2024-05-10 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='korisnik',
            name='korisnicko_ime',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
