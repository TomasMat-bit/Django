from django.test import TestCase
from ..models import Note

class NoteModeTest(TestCase):
    def test_note_creation(self):
        note = Note.objects.create(title='Testas', content='Turinys')

        self.assertEquals(note.title, 'Testas')

        self.assertEqual(note.content, 'Turinys')

    def test_str_method(self):
        note = Note.objects.create(title='Testas')
        self.assertEqual(str(note), note.title)

