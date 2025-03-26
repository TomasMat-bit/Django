from django.shortcuts import render, redirect
from .forms import RegistracijaForma
from .models import Registracija

def registracija(request):
    if request.method == 'POST':
        forma = RegistracijaForma(request.POST)
        if forma.is_valid():
            forma.save()  # Išsaugome naują registraciją
            return redirect('dalyviai')  # Peradresuojame į dalyvių sąrašą
    else:
        forma = RegistracijaForma()

    return render(request, 'registracija.html', {'forma': forma})

def dalyviai(request):
    registracijos = Registracija.objects.all()  # Gaukite visus užsiregistravusius žmones
    return render(request, 'dalyviai.html', {'registracijos': registracijos})
