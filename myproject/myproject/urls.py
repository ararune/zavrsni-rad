# urls.py
from django.contrib import admin
from django.urls import path
from myapp.views import registriraj_korisnika, pocetna, profil, gradovi_po_zupaniji, kreiraj_oglas, moji_oglasi, oglasi_po_kategoriji, oglas_detalji
from django.contrib.auth import views as auth_views
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('registracija/', registriraj_korisnika, name='registracija'),
    path('prijava/', auth_views.LoginView.as_view(template_name='prijava.html', success_url='/'), name='prijava'),
    path('odjava/', auth_views.LogoutView.as_view(next_page='/'), name='odjava'),
    path('profil/', profil, name='profil'),
    path('gradovi_po_zupaniji/', gradovi_po_zupaniji, name='gradovi_po_zupaniji'),
    path('kreiraj_oglas/', kreiraj_oglas, name='kreiraj_oglas'),
    path('moji_oglasi/', moji_oglasi, name='moji_oglasi'),
    path('<str:url>/', oglasi_po_kategoriji, name='oglasi_po_kategoriji'),
    path('<str:kategorija_url>/<str:oglas_naziv>-oglas-<str:sifra>/', oglas_detalji, name='oglas_detalji'),
    path('', pocetna, name='pocetna'),
]
