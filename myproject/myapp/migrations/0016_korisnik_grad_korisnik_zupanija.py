# Generated by Django 5.0.6 on 2024-05-13 21:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_zupanija_grad'),
    ]

    operations = [
        migrations.AddField(
            model_name='korisnik',
            name='grad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.grad'),
        ),
        migrations.AddField(
            model_name='korisnik',
            name='zupanija',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.zupanija'),
        ),
    ]
