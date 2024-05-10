# models.py
from django.db import models

class Korisnik(models.Model):
    korisnicko_ime = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)