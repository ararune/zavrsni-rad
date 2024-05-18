""" views.py """
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Grad, Oglas, Kategorija, Slika
from .forms import FormaZaIzraduKorisnika, FormaZaIzraduOglasa
import base64


def registriraj_korisnika(request):
    if request.method == 'POST':
        form = FormaZaIzraduKorisnika(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
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


def oglasi_po_kategoriji(request, url):
    kategorija = get_object_or_404(Kategorija, url=url)

    def dohvati_podkategorije(kategorija):
        potkategorije = [kategorija]
        for dijete in kategorija.children.all():
            potkategorije.extend(dohvati_podkategorije(dijete))
        return potkategorije

    potkategorije = dohvati_podkategorije(kategorija)
    oglasi = Oglas.objects.filter(kategorija__in=potkategorije)

    hijerarhija = []
    trenutna_kategorija = kategorija
    while trenutna_kategorija:
        hijerarhija.insert(0, trenutna_kategorija)
        trenutna_kategorija = trenutna_kategorija.roditelj

    return render(request, 'oglasi_po_kategoriji.html', {'kategorija': kategorija, 'oglasi': oglasi, 'hijerarhija': hijerarhija})


def oglas_detalji(request, kategorija_url, oglas_naziv, sifra):
    oglas = get_object_or_404(Oglas, sifra=sifra)
    slike = oglas.slike.all()

    hijerarhija = []
    trenutna_kategorija = oglas.kategorija
    while trenutna_kategorija:
        hijerarhija.insert(0, trenutna_kategorija)
        trenutna_kategorija = trenutna_kategorija.roditelj

    return render(request, 'oglas_detalji.html', {'oglas': oglas, 'slike': slike, 'hijerarhija': hijerarhija})

@login_required
def uredi_oglas(request, kategorija_url, oglas_naziv, sifra):
    oglas = get_object_or_404(Oglas, sifra=sifra)

    if request.method == 'POST':
        form = FormaZaIzraduOglasa(request.POST, request.FILES, instance=oglas)
        if form.is_valid():
            # Handle image deletion
            if 'delete_slike' in request.POST:
                slike_to_delete_ids = request.POST.getlist('delete_slike')
                oglas.slike.filter(id__in=slike_to_delete_ids).delete()
            oglas = form.save(commit=False)
            for img in request.FILES.getlist('slike'):
                img_str = base64.b64encode(img.read()).decode('utf-8')
                Slika.objects.create(oglas=oglas, slika=img_str)
            oglas.save()
            return redirect('moji_oglasi')
    else:
        form = FormaZaIzraduOglasa(instance=oglas)

    return render(request, 'uredi_oglas.html', {'form': form})

@login_required
def izbrisi_oglas(request, oglas_id):
    oglas = get_object_or_404(Oglas, id=oglas_id)
    if request.method == 'POST':
        oglas.delete()
        return redirect('moji_oglasi')
    return redirect('moji_oglasi')  # Redirect to moji_oglasi if the request method is not POST
