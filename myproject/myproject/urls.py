# urls.py
from django.contrib import admin
from django.urls import path
from myapp.views import registriraj_korisnika, pocetna, profil, gradovi_po_zupaniji, kreiraj_oglas
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('registracija/', registriraj_korisnika, name='registracija'),
    path('prijava/', auth_views.LoginView.as_view(template_name='prijava.html', success_url='/'), name='prijava'),
    path('odjava/', auth_views.LogoutView.as_view(next_page='/'), name='odjava'),
    path('profil/', profil, name='profil'),
    path('gradovi_po_zupaniji/', gradovi_po_zupaniji, name='gradovi_po_zupaniji'),
    path('kreiraj_oglas/', kreiraj_oglas, name='kreiraj_oglas'),
    path('', pocetna, name='pocetna'),
]
