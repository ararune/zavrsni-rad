# Generated by Django 5.0.6 on 2024-05-13 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_remove_korisnik_oib_alter_korisnik_password_and_more'),
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
        migrations.AlterModelOptions(
            name='korisnik',
            options={},
        ),
        migrations.AlterModelManagers(
            name='korisnik',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='korisnik',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='korisnik',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='korisnik',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='korisnik',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='korisnik',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='korisnik',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='korisnik',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='korisnik',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='korisnik',
            name='password',
        ),
        migrations.RemoveField(
            model_name='korisnik',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='korisnik',
            name='username',
        ),
        migrations.DeleteModel(
            name='Grad',
        ),
        migrations.DeleteModel(
            name='Zupanija',
        ),
    ]