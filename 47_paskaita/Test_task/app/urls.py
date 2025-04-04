from django.urls import path
from . import views
from .views import NoteUpdateView, NoteDeleteView

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('create/', views.create_note, name='create_note'),
    path('note/<int:pk>/edit/', NoteUpdateView.as_view(), name='edit_note'),
    path('note/<int:pk>/delete/', NoteDeleteView.as_view(), name='delete_note'),

]



