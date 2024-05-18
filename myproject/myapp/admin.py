# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Korisnik, Zupanija, Grad, Kategorija, Oglas, Slika
from django.utils.html import format_html

class KorisnikAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'grad')

class KategorijaAdmin(admin.ModelAdmin):
    list_display = ('naziv', 'roditelj', 'url')

class GradAdmin(admin.ModelAdmin):
    list_display = ('naziv', 'zupanija')
    
class OglasAdmin(admin.ModelAdmin):
    list_display = ('naziv', 'kategorija', 'cijena', 'sifra', 'korisnik', 'zupanija', 'grad', 'trajanje')


admin.site.register(Korisnik, KorisnikAdmin)
admin.site.register(Zupanija)
admin.site.register(Grad, GradAdmin)
admin.site.register(Kategorija, KategorijaAdmin)
admin.site.register(Oglas, OglasAdmin)
