# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required  # Add this import
from django.http import JsonResponse
from .models import Grad, Oglas, Kategorija, Slika
import base64
from django.core.files.base import ContentFile



from .forms import FormaZaIzraduKorisnika, FormaZaIzraduOglasa
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

@login_required
def profil(request):
    korisnik = request.user
    return render(request, 'profil.html', {'korisnik': korisnik})

def gradovi_po_zupaniji(request):
    zupanija_id = request.GET.get('zupanija_id')
    gradovi = Grad.objects.filter(zupanija_id=zupanija_id)
    data = [{'id': grad.id, 'naziv': grad.naziv} for grad in gradovi]
    return JsonResponse(data, safe=False)


@login_required
def kreiraj_oglas(request):
    if request.method == 'POST':
        form = FormaZaIzraduOglasa(request.POST, request.FILES)
        if form.is_valid():
            oglas = form.save(commit=False)
            oglas.korisnik = request.user
            oglas.save()
            for img in request.FILES.getlist('slike'):
                # Enkodiranje slike u base64 za pohranu
                img_str = base64.b64encode(img.read()).decode('utf-8')
                Slika.objects.create(oglas=oglas, slika=img_str)
            return redirect('pocetna')
    else:
        form = FormaZaIzraduOglasa()
    return render(request, 'kreiraj_oglas.html', {'form': form})


@login_required
def moji_oglasi(request):
    oglasi = Oglas.objects.filter(korisnik=request.user)
    return render(request, 'moji_oglasi.html', {'oglasi': oglasi})

def oglasi_po_kategoriji(request, naziv):
    kategorija = get_object_or_404(Kategorija, naziv=naziv)

    # Rek. Funkcija za dohvaćanje svih potkategorija
    def dohvati_potkategorije(kategorija):
        potkategorije = [kategorija]
        for dijete in kategorija.children.all():
            potkategorije.extend(dohvati_potkategorije(dijete))
        return potkategorije

    potkategorije = dohvati_potkategorije(kategorija)

    # Filtriranje objekata Oglas na temelju potkategorija
    oglasi = Oglas.objects.filter(kategorija__in=potkategorije)
    
    return render(request, 'oglasi_po_kategoriji.html', {'kategorija': kategorija, 'oglasi': oglasi})