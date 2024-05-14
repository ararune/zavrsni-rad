# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Korisnik, Zupanija, Grad

class KorisnikAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'oib', 'zupanija', 'grad')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'oib', 'zupanija', 'grad', 'is_staff', 'is_superuser'),
        }),
    )
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

admin.site.register(Korisnik, KorisnikAdmin)
admin.site.register(Zupanija)
admin.site.register(Grad)