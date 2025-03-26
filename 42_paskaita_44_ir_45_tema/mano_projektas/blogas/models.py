from django.db import models

class Registracija(models.Model):
    vardas = models.CharField(max_length=100)
    el_pastas = models.EmailField(unique=True)  # Unikalus el. pašto adresas
    registracijos_data = models.DateTimeField(auto_now_add=True)  # Automatiškai nustatoma data ir laikas

    def __str__(self):
        return f"{self.vardas} ({self.el_pastas})"
