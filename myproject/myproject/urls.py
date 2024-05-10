# urls.py
from django.contrib import admin
from django.urls import path
from myapp.views import registriraj_korisnika, pocetna
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registracija/', registriraj_korisnika, name='registracija'),
    path('prijava/', auth_views.LoginView.as_view(template_name='prijava.html', success_url='/pocetna/'), name='prijava'),
    path('', pocetna, name='pocetna'),
]
