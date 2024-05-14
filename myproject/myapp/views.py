# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required  # Add this import

from .forms import FormaZaIzraduKorisnika
def registriraj_korisnika(request):
    if request.method == 'POST':
        form = FormaZaIzraduKorisnika(request.POST)
        if form.is_valid():
            user = form.save()
            # Log in the user after registration
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # Redirect to pocetna after successful registration and login
            return redirect('pocetna')
    else:
        form = FormaZaIzraduKorisnika()
    return render(request, 'registracija.html', {'form': form})


def pocetna(request):
    korisnik = request.user
    return render(request, 'pocetna.html', {'korisnik': korisnik})


