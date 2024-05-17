# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Korisnik, Zupanija, Grad, Oglas, Slika
from django.core.exceptions import ValidationError


class FormaZaIzraduKorisnika(UserCreationForm):
    zupanija = forms.ModelChoiceField(queryset=Zupanija.objects.all(), empty_label="Odaberi županiju", required=True)
    grad = forms.ModelChoiceField(queryset=Grad.objects.none(), empty_label="Odaberi grad", required=False)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Korisnik
        fields = ['username', 'email', 'password1', 'password2', 'oib', 'zupanija', 'grad']
        widgets = {
            'password1': forms.PasswordInput(),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def clean(self):
        cleaned_data = super().clean()
        for field_name in self.Meta.fields:
            if not cleaned_data.get(field_name):
                self.add_error(field_name, f'This field is required.')
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'zupanija' in self.data:
            try:
                zupanija_id = int(self.data.get('zupanija'))
                self.fields['grad'].queryset = Grad.objects.filter(zupanija_id=zupanija_id)
            except (ValueError, TypeError):
                pass  # invalid input od korisnika
        elif self.instance.pk:
            self.fields['grad'].queryset = self.instance.zupanija.grad_set.none()

class VisestrukiUnosDatoteka(forms.ClearableFileInput):
    allow_multiple_selected = True

class VisestrukaDatoteka(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", VisestrukiUnosDatoteka())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        ciscenje_jedne_datoteke = super().clean
        if isinstance(data, (list, tuple)):
            rezultat = [ciscenje_jedne_datoteke(d, initial) for d in data]
        else:
            rezultat = ciscenje_jedne_datoteke(data, initial)
        return rezultat

class SlikaForma(forms.ModelForm):
    slike = VisestrukaDatoteka(label='Odaberi datoteke', required=False)

    class Meta:
        model = Slika
        fields = ['slike', ]

class FormaZaIzraduOglasa(forms.ModelForm):
    MAX_VELICINA_SLIKE = 5 * 1024 * 1024  # 5MB u bytovima
    MAX_BROJ_SLIKA = 4

    slike = VisestrukaDatoteka(label='Odaberi slike', required=False)

    class Meta:
        model = Oglas
        fields = ['cijena', 'naziv', 'opis', 'zupanija', 'grad', 'trajanje', 'kategorija', 'slike']

    def clean_slike(self):
        slike = self.cleaned_data.get('slike')
        if len(slike) > self.MAX_BROJ_SLIKA:
            raise ValidationError(f'Možete odabrati maksimalno {self.MAX_BROJ_SLIKA} slike.')

        for img in slike:
            if img.size > self.MAX_VELICINA_SLIKE:
                raise ValidationError('Slika ne smije biti veća od 5MB.')
        
        return slike
