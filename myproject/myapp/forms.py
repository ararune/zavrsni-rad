# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Korisnik, Zupanija, Grad, Oglas


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
                pass  # invalid input from the client; ignore and fallback to empty Grad queryset
        elif self.instance.pk:
            self.fields['grad'].queryset = self.instance.zupanija.grad_set.none()

class FormaZaIzraduOglasa(forms.ModelForm):
    class Meta:
        model = Oglas
        fields = ['cijena', 'naziv', 'opis', 'zupanija', 'grad', 'trajanje', 'kategorija']