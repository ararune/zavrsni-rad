# views.py
from django.shortcuts import render, redirect
from .forms import FormaZaRegistracijuKorisnika
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

def registriraj_korisnika(request):
    if request.method == 'POST':
        form = FormaZaRegistracijuKorisnika(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # Redirect to the 'pocetna' page or any other page you prefer
            return redirect('pocetna')
    else:
        form = FormaZaRegistracijuKorisnika()
    return render(request, 'registracija.html', {'form': form})


def pocetna(request):
    korisnik = request.user
    return render(request, 'pocetna.html', {'korisnik': korisnik})
