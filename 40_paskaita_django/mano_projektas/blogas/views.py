from django.db.models.fields import return_None
from django.shortcuts import render
from django.http import HttpResponse

def pagrindinis(request):
    kontekstas = {
        'pavadinimas': 'Mano Puslapis',
        'antraste': 'Sveiki atvyke i pagrindini puslapi'
    }
    return render(request, 'pagrindinis.html', kontekstas)

def apie(request):
    kontekstas = {
        'pavadinimas': 'Apie mus',
        'antraste': 'Informacija apie mus'
    }
    return render(request, 'apie.html', kontekstas)

def kontaktai(request):
    return HttpResponse('Susisiekite su mumis!')

def naujienos(request):
    kontekstas = {
        'pavadinimas': 'Naujienos',
        'antraste': 'Šviežiausios naujienos'
    }
    return render(request, 'naujienos.html', kontekstas)

def autorius(request):
    kontekstas = {
        'vardas' : 'Jonas',
        'pomegiai' : ['Programavimas', 'Dviraciai', 'Kava'],
    }
    return render(request, 'autorius.html', kontekstas)

