# Generated by Django 5.0.2 on 2024-05-10 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Korisnik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('korisnicko_ime', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('lozinka', models.CharField(max_length=100)),
            ],
        ),
    ]
