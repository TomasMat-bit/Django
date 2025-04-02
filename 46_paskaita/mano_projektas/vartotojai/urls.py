from django.urls import path
from . import views

urlpatterns = [
    path('profilis/', views.redaguoti_profili, name='profilis')
]