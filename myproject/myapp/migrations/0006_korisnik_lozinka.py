# Generated by Django 5.0.2 on 2024-05-10 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_korisnik_lozinka'),
    ]

    operations = [
        migrations.AddField(
            model_name='korisnik',
            name='lozinka',
            field=models.CharField(default='', max_length=100),
        ),
    ]