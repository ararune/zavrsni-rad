# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class Zupanija(models.Model):
    naziv = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.naziv

class Grad(models.Model):
    naziv = models.CharField(max_length=100)
    zupanija = models.ForeignKey(Zupanija, on_delete=models.CASCADE)

    def __str__(self):
        return self.naziv

class Korisnik(AbstractUser):
    oib = models.CharField(max_length=11, null=True, validators=[RegexValidator(r'^\d{11}$', message='OIB must be exactly 11 digits')])
    zupanija = models.ForeignKey(Zupanija, on_delete=models.CASCADE, null=True)
    grad = models.ForeignKey(Grad, on_delete=models.CASCADE, null=True)


    # Specifying related_name to avoid clashes with the built-in User model
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_set', blank=True)

    class Meta:
        verbose_name = 'Korisnik'
        verbose_name_plural = 'Korisnici'

    def __str__(self):
        return self.username
