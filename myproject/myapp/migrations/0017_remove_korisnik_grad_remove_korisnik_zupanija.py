# Generated by Django 5.0.6 on 2024-05-13 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_korisnik_grad_korisnik_zupanija'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='korisnik',
            name='grad',
        ),
        migrations.RemoveField(
            model_name='korisnik',
            name='zupanija',
        ),
    ]
