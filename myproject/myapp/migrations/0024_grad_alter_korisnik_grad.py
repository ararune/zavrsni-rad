# Generated by Django 5.0.6 on 2024-05-14 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_korisnik_grad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=100)),
                ('zupanija', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.zupanija')),
            ],
        ),
        migrations.AlterField(
            model_name='korisnik',
            name='grad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.grad'),
        ),
    ]
