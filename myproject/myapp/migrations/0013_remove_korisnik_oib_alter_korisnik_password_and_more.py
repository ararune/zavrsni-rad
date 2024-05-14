# Generated by Django 5.0.6 on 2024-05-13 16:58

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_korisnik_options_alter_korisnik_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='korisnik',
            name='oib',
        ),
        migrations.AlterField(
            model_name='korisnik',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='korisnik',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
