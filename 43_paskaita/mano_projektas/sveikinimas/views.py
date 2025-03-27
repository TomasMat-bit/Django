from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from .forms import RegistracijosForma

def registracija(request):
    if request.method == "POST":
        form = RegistracijosForma(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prisijungti')
    else:
        form = RegistracijosForma()
    return render(request, 'sveikinimas/registracija.html', {'form': form})

def prisijungti(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('pagrindinis')
    else:
        form = AuthenticationForm()
    return render(request, 'sveikinimas/prisijungti.html', {'form': form})

@login_required
def pagrindinis(request):
    return render(request, 'sveikinimas/pagrindinis.html')

class AtsijungtiView(LogoutView):
    next_page = '/'
