from django.test import TestCase
from django.urls import reverse
from app.models import Note

class NoteViewTest(TestCase):
    def test_note_list_view(self):
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)

    def test_create_note_view(self):
        response = self.client.get(reverse('create_note'))
        self.assertEqual(response.status_code, 200)

    def test_create_note_post(self):
        data = {'title': 'New Note', 'content': 'Note content'}
        response = self.client.post(reverse('create_note'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 1)