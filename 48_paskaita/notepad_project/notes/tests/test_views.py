from http.client import responses

from django.test import TestCase
from django.urls import reverse
from .. models import Note

class NoteViewTest(TestCase):
    def test_note_list_view(self):
        response = self.client.get(reverse('note_list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'note_list.html')

    def test_note_create_view_get(self):
        response = self.client.get(reverse('note_create'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'note_form.html')

    def test_note_create_view_get(self):
        data = {
            'title': 'Testinis',
            'content': 'Testinis turinys'
        }
        response = self.client.post(reverse('note_create'), data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 1)

