from django.urls import path
from . import views

urlpatterns = [
    path('registracija/', views.registracija, name='registracija'),
    path('prisijungti/', views.prisijungti, name='prisijungti'),
    path('', views.pagrindinis, name='pagrindinis'),
    path('atsijungti/', views.AtsijungtiView.as_view(), name='atsijungti'),
]
