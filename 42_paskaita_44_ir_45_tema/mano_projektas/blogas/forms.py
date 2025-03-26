from django import forms
from .models import Registracija

class RegistracijaForma(forms.ModelForm):
    class Meta:
        model = Registracija
        fields = ['vardas', 'el_pastas']  # Formoje bus tik vardas ir el. paštas

    def clean_el_pastas(self):
        el_pastas = self.cleaned_data.get('el_pastas')
        if Registracija.objects.filter(el_pastas=el_pastas).exists():
            raise forms.ValidationError('Šiuo el. paštu jau užsiregistruota.')
        return el_pastas
