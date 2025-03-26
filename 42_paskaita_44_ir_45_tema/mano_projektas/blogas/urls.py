from django.urls import path
from . import views


urlpatterns = [
    path('registracija/', views.registracija, name='registracija'),
    path('dalyviai/', views.dalyviai, name='dalyviai'),
]
