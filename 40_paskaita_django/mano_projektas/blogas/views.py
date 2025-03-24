from django.shortcuts import render
from django.http import HttpResponse

def pagrindinis(request):
    kontekstas = {
        'pavadinimas': 'Mano Puslapis',
        'antraste': 'Sveiki atvyke i pagrindini puslapi'
    }
    return render(request, 'pagrindinis.html', kontekstas)

def apie(request):
    return HttpResponse('Cia yra apie puslapis')
